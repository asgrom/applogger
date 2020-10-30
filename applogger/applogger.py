"""Logger for module."""
import logging
from logging.handlers import RotatingFileHandler
import os

FORMATTER = '%(asctime)s [%(levelname)s] (%(name)s - %(filename)s.%(funcName)s(%(lineno)d)): %(message)s'
LOG_FILE = os.path.join(os.path.dirname(__name__), 'app.log')


def get_file_handler():
    f_handler = RotatingFileHandler(LOG_FILE, maxBytes=500000)
    f_handler.setLevel(logging.DEBUG)
    f_handler.setFormatter(logging.Formatter(FORMATTER))
    return f_handler


def get_stream_logger():
    f_handler = logging.StreamHandler()
    f_handler.setLevel(logging.ERROR)
    f_handler.setFormatter(logging.Formatter(FORMATTER))
    return f_handler


def get_logger(name):
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    logger.addHandler(get_file_handler())
    logger.addHandler(get_stream_logger())
    return logger


def set_log_file(file):
    global LOG_FILE
    LOG_FILE = file


if __name__ == '__main__':
    get_logger(__name__)
