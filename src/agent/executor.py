import io
import contextlib
import traceback
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def execute_code(code: str, df: pd.DataFrame) -> dict:
    """
    Execute generated Python code against the dataframe and capture output.
    """
    output_buffer = io.StringIO()

    safe_globals = {
        "__builtins__": {
            "print": print,
            "len": len,
            "range": range,
            "min": min,
            "max": max,
            "sum": sum,
            "abs": abs,
            "sorted": sorted,
            "round": round,
        }
    }

    local_vars = {
        "df": df.copy(),
        "pd": pd,
        "np": np,
        "plt": plt,
    }

    cleaned_code = code.replace("import pandas as pd", "")
    cleaned_code = cleaned_code.replace("import numpy as np", "")
    cleaned_code = cleaned_code.replace("import matplotlib.pyplot as plt", "")

    try:
        plt.close("all")

        with contextlib.redirect_stdout(output_buffer):
            exec(cleaned_code, safe_globals, local_vars)

        figure = plt.gcf() if plt.get_fignums() else None

        return {
            "success": True,
            "output": output_buffer.getvalue(),
            "error": None,
            "figure": figure,
        }

    except Exception:
        return {
            "success": False,
            "output": output_buffer.getvalue(),
            "error": traceback.format_exc(),
            "figure": None,
        }