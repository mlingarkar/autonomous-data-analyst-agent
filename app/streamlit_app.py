import os
import sys

import streamlit as st
import matplotlib.pyplot as plt

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(CURRENT_DIR)

if PROJECT_ROOT not in sys.path:
    sys.path.append(PROJECT_ROOT)

from src.data.loader import load_data
from src.data.summarizer import summarize_data
from src.config import Config
from src.agent.agent import DataAnalystAgent

st.set_page_config(page_title="Autonomous Data Analyst Agent", layout="wide")

st.title("Autonomous Data Analyst Agent")
st.write("Upload a CSV, ask questions, and get automated analysis, insights, and ML-ready outputs.")

uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

if "agent" not in st.session_state:
    st.session_state.agent = DataAnalystAgent()

if uploaded_file is not None:
    try:
        df = load_data(uploaded_file)
        summary = summarize_data(df)

        st.subheader("Dataset Preview")
        st.dataframe(df.head(Config.PREVIEW_ROWS), width="stretch")

        st.subheader("Dataset Summary")
        st.json(summary)

        st.subheader("Ask a Question")

        with st.form("question_form"):
            user_question = st.text_input("What would you like to know about this dataset?")
            submitted = st.form_submit_button("Run Agent")

        if submitted:
            if not user_question.strip():
                st.warning("Please enter a question first.")
            else:
                with st.spinner("Generating analysis..."):
                    response = st.session_state.agent.run(df, summary, user_question)

                st.caption(f"Mode: {response['mode']}")
                st.caption(f"Retries used: {response['retries_used']}")

                if response["mode"] == "analysis":
                    st.subheader("Generated Code")
                    st.code(response["code"], language="python")

                if response["result"]["success"]:
                    st.subheader("Execution Output")
                    st.text(response["result"]["output"] or "Code ran successfully with no printed output.")

                    if response["insights"]:
                        st.subheader("Business Insights")
                        st.write(response["insights"])

                    if response["mode"] == "ml" and "feature_importance_df" in response:
                        st.subheader("Top Feature Importances")
                        st.dataframe(response["feature_importance_df"], width="stretch")

                        fig, ax = plt.subplots(figsize=(10, 5))
                        feature_df = response["feature_importance_df"].sort_values("importance", ascending=True)
                        ax.barh(feature_df["feature"], feature_df["importance"])
                        ax.set_title("Top Feature Importances")
                        ax.set_xlabel("Importance")
                        ax.set_ylabel("Feature")
                        plt.tight_layout()
                        st.pyplot(fig)

                    if response["result"]["figure"] is not None:
                        st.subheader("Visualization")
                        st.pyplot(response["result"]["figure"])

                    st.subheader("Recent Session Memory")
                    st.code(st.session_state.agent.memory.get_recent_context(), language="text")
                else:
                    st.subheader("Execution Error")
                    st.error(response["result"]["error"])

    except Exception as e:
        st.error(f"Error loading file: {e}")
else:
    st.info("Upload a CSV file to begin.")