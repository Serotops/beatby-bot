import logging
from logging.handlers import RotatingFileHandler
from .formatter import LoggingFormatter

def setup_logger():
    logger = logging.getLogger("discord_bot")
    logger.setLevel(logging.INFO)

    # Console handler remains unchanged
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(LoggingFormatter())
    
    # Replace FileHandler with RotatingFileHandler
    file_handler = RotatingFileHandler(
        filename="discord.log",
        encoding="utf-8",
        maxBytes=5 * 1024 * 1024,  # 5MB per file
        backupCount=5              # Keep 5 backup files
    )
    file_handler_formatter = logging.Formatter(
        "[{asctime}] [{levelname:<8}] {name}: {message}", 
        "%Y-%m-%d %H:%M:%S", 
        style="{"
    )
    file_handler.setFormatter(file_handler_formatter)

    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

    return logger