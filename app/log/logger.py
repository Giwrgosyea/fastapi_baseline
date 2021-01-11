import logging
from pathlib import Path
from logging.handlers import RotatingFileHandler


class Logger:
    def __init__(self, name):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.INFO)

        formatter = logging.Formatter(
            "(%(asctime)s) [%(levelname)s] %(name)s:%(funcName)s:%(message)s:line %(lineno)d"
        )

        Path("./logs").mkdir(exist_ok=True)

        file_handler = logging.handlers.RotatingFileHandler(
            "./logs/log_file.log", maxBytes=1024 * 1024 * 100, backupCount=20
        )
        file_handler.setLevel(logging.INFO)
        file_handler.setFormatter(formatter)
        self.logger.addHandler(file_handler)
        self.logger.propagate = False

    def get_logger(self):
        return self.logger