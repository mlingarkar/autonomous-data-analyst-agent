import pandas as pd


def prepare_regression_data(df: pd.DataFrame, target_column: str):
    """
    Prepare features and target for a regression model.
    - Drops rows with missing target
    - One-hot encodes categorical columns
    - Keeps numeric columns as-is
    """
    if target_column not in df.columns:
        raise ValueError(f"Target column '{target_column}' not found in dataset.")

    model_df = df.copy()

    model_df = model_df.dropna(subset=[target_column])

    X = model_df.drop(columns=[target_column])
    y = model_df[target_column]

    X_encoded = pd.get_dummies(X, drop_first=True)

    return X_encoded, y