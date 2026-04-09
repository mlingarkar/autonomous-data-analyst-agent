def analysis_prompt(summary: dict, question: str) -> str:
    return f"""
You are a senior data analyst helping a user understand their dataset.

Dataset summary:
{summary}

User question:
{question}

Instructions:
- Answer clearly in plain English
- Be specific to the dataset summary provided
- If the question cannot be fully answered from the summary alone, say that more detailed row-level analysis is needed
- Suggest what analysis should be run next
"""


def code_generation_prompt(summary: dict, question: str) -> str:
    return f"""
You are an expert Python data analyst.

Dataset summary:
{summary}

User question:
{question}

Write Python code that analyzes the dataframe named df.

Important:
- The dataframe is already loaded as df
- pandas is already available as pd
- numpy is already available as np
- matplotlib.pyplot is already available as plt
- DO NOT import anything
- DO NOT load any files
- DO NOT use input()
- Print useful results clearly
- Create a matplotlib chart if it helps answer the question
- Return ONLY executable Python code
- Do not include markdown fences
"""


def code_fix_prompt(summary: dict, question: str, bad_code: str, error_message: str) -> str:
    return f"""
You are fixing Python analysis code.

Dataset summary:
{summary}

User question:
{question}

The following code failed:

{bad_code}

This was the error:

{error_message}

Please return corrected Python code.

Rules:
- The dataframe is already loaded as df
- pandas is already available as pd
- numpy is already available as np
- matplotlib.pyplot is already available as plt
- DO NOT import anything
- DO NOT load files
- Return ONLY executable Python code
- Do not include markdown fences
"""


def insight_prompt(question: str, output: str) -> str:
    return f"""
You are a senior business data analyst.

The user asked:
{question}

The analysis output was:
{output}

Write 3 to 5 concise business insights.

Rules:
- Use bullet points
- Be specific
- Mention important numbers when available
- Keep it plain English
- Do not mention code
"""