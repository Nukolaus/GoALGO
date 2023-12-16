import logging
import sys
from logging import Handler, Logger
from typing import Literal

from config.settings import settings

ENABLED_HANDLERS = {
    "console_handler": True,
    "file_handler": False,
    "telegram_handler": False,
}

log_level_aliases = {
    "D": logging.DEBUG,
    "I": logging.INFO,
    "W": logging.WARNING,
    "E": logging.ERROR,
    "C": logging.CRITICAL,
}


def create_console_handler() -> Handler:
    """Function to create console handler for logging"""
    formatter = logging.Formatter(
        fmt='[{levelname:<8}] [{name}:{funcName}:{lineno}]: "{message}"',
        style="{",
    )

    handler = logging.StreamHandler(stream=sys.stdout)
    handler.setLevel(logging.DEBUG)
    handler.setFormatter(formatter)

    return handler


def create_file_handler() -> Handler:
    """Function to create file handler for logging"""
    formatter = logging.Formatter(
        fmt='[{levelname:<10}: {asctime}] \
                        [{name}:{funcName}:{lineno}]: "{message}"',
        style="{",
    )

    handler = logging.FileHandler(filename=settings.log_file, encoding="utf-8")
    handler.setLevel(logging.INFO)
    handler.setFormatter(formatter)
    return handler


def conf_logger(
    logger_name: str,
    log_level: Literal["C", "E", "W", "I", "D", "N"] = "E",
    capture_warnins: bool = False,  # noqa: FBT
) -> Logger:
    """Function to create configured_logger"""

    logging.captureWarnings(capture=capture_warnins)

    logger = logging.getLogger(logger_name)
    logger.setLevel(log_level_aliases[log_level])

    handlers = (
        create_console_handler(),
        create_file_handler(),
    )

    [logger.addHandler(handler) for handler in handlers]
    return logger


