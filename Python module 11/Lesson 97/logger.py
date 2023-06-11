import logging
from logging.handlers import RotatingFileHandler

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
handler = RotatingFileHandler('logs.log', mode='a', encoding='utf-8', maxBytes=262144, backupCount=5)
formatter = logging.Formatter('%(levelname)s %(asctime)s %(message)s', datefmt='%d/%m/%Y %H:%M:%S')
handler.setFormatter(formatter)
logger.addHandler(handler)
