import pandas as pd


def find_similar_columns(df: pd.DataFrame, keyword: str) -> list[str]:
    """
    Return column names that loosely match a keyword.
    Helpful for dynamic target detection or validation.
    """
    keyword_lower = keyword.lower().strip()
    return [col for col in df.columns if keyword_lower in col.lower()]


def validate_column_exists(df: pd.DataFrame, column_name: str) -> None:
    """
    Raise a helpful error if a required column is missing.
    """
    if column_name not in df.columns:
        available = ", ".join(df.columns)
        raise ValueError(
            f"Column '{column_name}' was not found in the dataset. "
            f"Available columns: {available}"
        )


def summarize_numeric_columns(df: pd.DataFrame) -> pd.DataFrame:
    """
    Return a quick summary of numeric columns.
    Useful for future analysis extensions.
    """
    numeric_df = df.select_dtypes(include=["number"])
    if numeric_df.empty:
        return pd.DataFrame()

    summary = numeric_df.describe().T
    summary["missing_values"] = numeric_df.isnull().sum()
    return summary


def clean_text_response(text: str) -> str:
    """
    Clean extra whitespace from model responses.
    """
    return "\n".join(line.rstrip() for line in text.strip().splitlines())