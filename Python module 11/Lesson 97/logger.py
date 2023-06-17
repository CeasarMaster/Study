import logging
import os
from logging.handlers import RotatingFileHandler

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
handler = RotatingFileHandler('logs.log', mode='a', encoding='utf-8', maxBytes=262144, backupCount=5)
formatter = logging.Formatter('%(levelname)s %(asctime)s %(message)s', datefmt='%d/%m/%Y %H:%M:%S')
handler.setFormatter(formatter)
logger.addHandler(handler)

directory = 'D:\Programming\Study\Python module 11'

for root, dirs, files in os.walk(directory):

    for filename in files:
        print(filename)
        file_path = os.path.join(root, filename)
        logger.info(f'Checking {file_path}...')
    logger.info('All files in directory correct...')
