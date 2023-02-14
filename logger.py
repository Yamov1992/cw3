
import logging


def config():

    api_logger = logging.getLogger('api_logger')
    api_logger.setLevel(logging.INFO)

    api_logger_handler = logging.FileHandler('logs/api.log', "w", encoding="UTF-8")
    api_logger_handler.setLevel(logging.INFO)
    api_logger.addHandler(api_logger_handler)

    api_logger_format = logging.Formatter('%(asctime)s [%(levelname)s] %(message)s')
    api_logger_handler.setFormatter(api_logger_format)