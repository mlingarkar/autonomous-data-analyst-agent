import logging
from pathlib import Path


def get_logger(name: str = "autonomous_data_analyst_agent") -> logging.Logger:
    """
    Create or return a configured logger for the project.
    Logs to both console and a local logs/app.log file.
    """
    logger = logging.getLogger(name)

    if logger.handlers:
        return logger

    logger.setLevel(logging.INFO)

    log_dir = Path("logs")
    log_dir.mkdir(exist_ok=True)
    log_file = log_dir / "app.log"

    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
    )

    file_handler = logging.FileHandler(log_file, encoding="utf-8")
    file_handler.setLevel(logging.INFO)
    file_handler.setFormatter(formatter)

    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.INFO)
    stream_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(stream_handler)

    return logger