import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.model_selection import train_test_split


def train_defect_count_model(X: pd.DataFrame, y: pd.Series) -> dict:
    """
    Train a random forest regressor and return metrics + feature importances.
    """
    if len(X) < 10:
        raise ValueError("Not enough rows to train a model. Need at least 10 rows.")

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model = RandomForestRegressor(
        n_estimators=150,
        random_state=42,
        n_jobs=-1
    )
    model.fit(X_train, y_train)

    predictions = model.predict(X_test)

    mae = mean_absolute_error(y_test, predictions)
    rmse = np.sqrt(mean_squared_error(y_test, predictions))
    r2 = r2_score(y_test, predictions)

    importance_df = pd.DataFrame({
        "feature": X.columns,
        "importance": model.feature_importances_
    }).sort_values("importance", ascending=False)

    return {
        "model": model,
        "mae": mae,
        "rmse": rmse,
        "r2": r2,
        "feature_importance": importance_df.head(10),
        "X_test": X_test,
        "y_test": y_test,
        "predictions": predictions,
    }