# Autonomous Data Analyst Agent

An AI-powered Streamlit application that allows users to upload a CSV dataset, ask questions in natural language, automatically generate Python analysis code, execute that code, visualize results, and receive business insights. The app also includes a machine learning mode for predictive analysis and feature importance reporting.

---

## Overview

The Autonomous Data Analyst Agent is designed to simulate an AI-assisted analytics workflow.

Instead of manually inspecting data, writing code, debugging analysis steps, and explaining results, users can interact with the application in plain English. The app then decides how to respond, generates the analysis logic, executes it against the uploaded dataset, and presents the results in a usable format.

This project combines:

- natural language interaction
- automated Python code generation
- code execution on uploaded data
- retry logic for code correction
- chart generation
- machine learning workflows
- business insight summary

This project goes beyond a standard dashboard or notebook analysis by combining natural language interaction, automated code generation, execution, visualization, and machine learning in a single workflow.

It demonstrates the ability to:

- translate business questions into executable analysis
- automate repetitive analyst workflows
- integrate LLMs into data applications
- build interactive tools using Python and Streamlit
- connect technical model outputs to business-facing insights
- create an end-to-end analytics workflow rather than just isolated scripts

---

## Project Features

### Dataset Upload and Summary
Users can upload a CSV file directly into the app. The application then provides:

- dataset preview
- dataset shape
- column names
- data types
- missing value counts
- numeric and categorical column summaries

### Natural Language Analysis
Users can ask business or analytical questions in plain English, such as:

- What are the top 5 defect types by total defect count?
- Which machines have the highest average defect count?
- Analyze whether operator level seems related to defect count.

### AI-Generated Python Analysis
The application uses an LLM to generate Python code tailored to the user’s question and the uploaded dataset summary.

### Code Execution Engine
Generated analysis code is executed automatically against the dataframe. The app captures:

- execution output
- errors
- matplotlib visualizations

### Retry / Self-Correction Loop
If generated code fails, the application sends the error back to the model and retries with corrected code automatically.

### Business Insight Generation
After successful execution, the app generates plain-English business insights based on the results.

### Machine Learning Mode
For predictive or modeling-related questions, the app switches into ML mode and:

- prepares features for modeling
- trains a regression model
- evaluates model performance
- reports top feature importances
- generates business interpretation of model results

### Session Memory
The app stores a history of recent questions, modes, and summarized outputs within the session, making the workflow more agent-like and easier to extend for follow-up analysis.

### Logging and Observability
The application includes structured logging to track user questions, retries, execution flow, and errors. Logs are written to both the console and a local log file for easier debugging and development.

---

## How It Works

### 1. Upload Data
The user uploads a CSV file through the Streamlit interface.

### 2. Summarize Dataset
The app builds a dataset summary including schema, data types, missing values, and feature categories.

### 3. Ask a Question
The user enters a natural language question about the dataset.

### 4. Route the Request
The application determines whether the question is:

- a standard data analysis request
- a machine learning / predictive modeling request

### 5. Run the Workflow

#### Analysis Mode
- generate Python analysis code
- execute code against the dataset
- retry automatically if execution fails
- display output and visualization
- generate business insights

#### ML Mode
- preprocess data for modeling
- train a regression model
- evaluate model performance
- compute feature importances
- display metrics and ML insights

---

## Example Questions

### Analysis Mode
- What are the top 5 defect types by total defect count?
- Which operators appear to have the highest defect counts?
- Show average defect rate by machine.
- Analyze whether operator level seems related to defect count.
- Which machines have the highest average defect count, and show a chart?

### ML Mode
- Can you build a model to predict defect count?
- Which features matter most for predicting defect count?
- Use machine learning to analyze defect count drivers.
- What variables are most important in predicting defect count?

---

## Output Examples

The application can produce several types of outputs depending on the question.

### Analysis Mode
- generated Python code
- execution output from the dataset
- visualizations such as bar charts
- retry count if the original code needed correction
- plain-English business insights

### ML Mode
- model performance metrics such as MAE, RMSE, and R²
- top feature importance rankings
- feature importance visualizations
- business interpretation of predictive drivers

Example outputs include:

- top 5 defect types by total defect count
- average defect count by operator level
- average defect rate by machine
- model-based ranking of the most important drivers of defect count

---

## Sample Use Cases

This project is useful for scenarios where users want to quickly explore structured datasets without manually writing all of the analysis logic.

Possible use cases include:

- manufacturing quality analysis
- defect and scrap pattern analysis
- operator or machine performance analysis
- exploratory analytics for business datasets
- simple predictive modeling for operational outcomes
- AI-assisted analytics demonstrations

---

## Limitations

This project is designed as a portfolio-ready prototype, so there are some current limitations:

- only a basic regression workflow is implemented
- generated code may still occasionally require retry attempts
- the application depends on OpenAI API access and credits
- some datasets may require additional preprocessing for best performance
- generated insights depend on the quality of the dataset and model response
- current UI is focused more on functionality than visuals

---

## Future Improvements

Potential next steps for expanding this project include:

- classification mode in addition to regression
- dynamic target selection for ML workflows
- downloadable reports or exported result summaries
- improved UI with tabs, filters, and cleaner layout
- memory / conversation history
- support for SQL and database sources in addition to CSV uploads
- cloud deployment for public demo access
- prompt boundary checks

---

## Tech Stack

- Python
- Streamlit
- Pandas
- NumPy
- Matplotlib
- scikit-learn
- OpenAI API
- python-dotenv

---

## Project Architecture

```text
Autonomous Data Analyst Agent/
│
├── app/
│   └── streamlit_app.py
│
├── src/
│   ├── config.py
│   │
│   ├── agent/
│   │   ├── agent.py
│   │   ├── executor.py
│   │   └── memory.py
│   │
│   ├── data/
│   │   ├── loader.py
│   │   └── summarizer.py
│   │
│   ├── llm/
│   │   ├── client.py
│   │   └── prompts.py
│   │
│   ├── ml/
│   │   ├── detect_task.py
│   │   ├── preprocess.py
│   │   ├── train.py
│   │   └── explain.py
│   │
│   └── utils/
│       ├── helpers.py
│       └── logger.py
│
└── README.md