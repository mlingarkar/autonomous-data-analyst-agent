from src.llm.client import ask_llm
from src.llm.prompts import code_generation_prompt, code_fix_prompt, insight_prompt
from src.agent.executor import execute_code
from src.agent.memory import SessionMemory
from src.ml.detect_task import is_ml_question
from src.ml.preprocess import prepare_regression_data
from src.ml.train import train_defect_count_model
from src.ml.explain import format_model_results
from src.utils.logger import get_logger
from src.utils.helpers import clean_text_response, validate_column_exists


class DataAnalystAgent:
    def __init__(self, max_retries: int = 2):
        self.max_retries = max_retries
        self.memory = SessionMemory()
        self.logger = get_logger()

    def run(self, df, summary: dict, question: str) -> dict:
        """
        Route either to analysis-code mode or ML mode.
        """
        self.logger.info("Received question: %s", question)

        if is_ml_question(question):
            response = self.run_ml_mode(df, question)
        else:
            response = self.run_analysis_mode(df, summary, question)

        output_summary = response["result"]["output"][:300] if response["result"]["output"] else "No output"
        self.memory.add_entry(question, response["mode"], output_summary)

        self.logger.info(
            "Completed question in mode=%s with retries=%s",
            response["mode"],
            response["retries_used"]
        )

        return response

    def run_analysis_mode(self, df, summary: dict, question: str) -> dict:
        prompt = code_generation_prompt(summary, question)
        code = ask_llm(prompt)
        result = execute_code(code, df)

        retries = 0

        while not result["success"] and retries < self.max_retries:
            self.logger.warning("Analysis execution failed. Retrying attempt %s", retries + 1)
            fix_prompt = code_fix_prompt(summary, question, code, result["error"])
            code = ask_llm(fix_prompt)
            result = execute_code(code, df)
            retries += 1

        insights = None
        if result["success"] and result["output"].strip():
            insights = clean_text_response(ask_llm(insight_prompt(question, result["output"])))

        return {
            "mode": "analysis",
            "question": question,
            "code": code,
            "result": result,
            "retries_used": retries,
            "insights": insights,
            "memory_context": self.memory.get_recent_context(),
        }

    def run_ml_mode(self, df, question: str) -> dict:
        """
        Run a regression model on Defect Count.
        """
        validate_column_exists(df, "Defect Count")

        X, y = prepare_regression_data(df, target_column="Defect Count")
        ml_results = train_defect_count_model(X, y)
        formatted_output = format_model_results(ml_results)

        insights = clean_text_response(
            ask_llm(
                insight_prompt(
                    question,
                    formatted_output
                )
            )
        )

        return {
            "mode": "ml",
            "question": question,
            "code": None,
            "result": {
                "success": True,
                "output": formatted_output,
                "error": None,
                "figure": None,
            },
            "retries_used": 0,
            "insights": insights,
            "feature_importance_df": ml_results["feature_importance"],
            "memory_context": self.memory.get_recent_context(),
        }