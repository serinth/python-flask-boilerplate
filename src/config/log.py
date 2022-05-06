import logging
from config.config import Config

def setup_logger(name: str, config: Config):
    formatter = logging.Formatter(fmt='%(asctime)s|%(levelname)s|%(filename)s:%(lineno)s|%(message)s')
    handler = logging.StreamHandler()
    handler.setFormatter(formatter)
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG if config.debug == True else logging.INFO)
    logger.addHandler(handler)    
    return logger