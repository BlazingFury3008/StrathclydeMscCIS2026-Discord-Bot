"""
This file is directly responsible for handling
the application's logging functionality.
"""

import logging
import sys
from pathlib import Path

from .config import LOGGING_DIRECTORY


# Configure logging directory
log_path = Path(LOGGING_DIRECTORY or "logs")
log_path.mkdir(parents=True, exist_ok=True)


# Configure logging formatter
logging_formatter = logging.Formatter(
    fmt="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)


# Configure file handler
logging_handler = logging.FileHandler(
    filename=log_path / "discord.log",
    encoding="utf-8",
    mode="a"
)

logging_handler.setFormatter(logging_formatter)


# Configure console handler
console_handler = logging.StreamHandler(sys.stdout)
console_handler.setFormatter(logging_formatter)


# Configure main logger
main_logger = logging.getLogger("discord_bot")
main_logger.setLevel(logging.DEBUG)

# Prevent duplicate logs through parent loggers
main_logger.propagate = False

# Attach handlers
main_logger.addHandler(logging_handler)
main_logger.addHandler(console_handler)