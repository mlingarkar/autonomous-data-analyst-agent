def format_model_results(results: dict) -> str:
    """
    Format model metrics and top feature importances into readable text.
    """
    lines = []
    lines.append("Model Performance:")
    lines.append(f"- MAE: {results['mae']:.3f}")
    lines.append(f"- RMSE: {results['rmse']:.3f}")
    lines.append(f"- R^2: {results['r2']:.3f}")
    lines.append("")
    lines.append("Top Feature Importances:")

    for _, row in results["feature_importance"].iterrows():
        lines.append(f"- {row['feature']}: {row['importance']:.4f}")

    return "\n".join(lines)