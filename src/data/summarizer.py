import pandas as pd


def summarize_data(df: pd.DataFrame) -> dict:
    """
    Return a compact summary of the uploaded dataset
    for display and later use by the LLM.
    """
    return {
        "shape": df.shape,
        "columns": list(df.columns),
        "dtypes": df.dtypes.astype(str).to_dict(),
        "missing_values": df.isnull().sum().to_dict(),
        "numeric_columns": df.select_dtypes(include=["number"]).columns.tolist(),
        "categorical_columns": df.select_dtypes(exclude=["number"]).columns.tolist(),
    }