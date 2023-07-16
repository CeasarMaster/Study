# [windows]
# directory = 'D:\Programming\Study\Python module 11'

import logging
import os
from logging.handlers import RotatingFileHandler
from configparser import ConfigParser
from sys import platform

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
handler = RotatingFileHandler('logs.log', mode='a', encoding='utf-8', maxBytes=262144, backupCount=5)
formatter = logging.Formatter('%(levelname)s %(asctime)s %(message)s', datefmt='%d/%m/%Y %H:%M:%S')
handler.setFormatter(formatter)
logger.addHandler(handler)
config = ConfigParser()
config.read('config.cfg')
    
if platform == 'darwin': 

    for root, dirs, files in os.walk('/Users/nikitadereza/PycharmProjects/Study/Python module 11'):
        for filename in files:
            file_path = os.path.join(root, filename)
            logger.info(f'Entering {file_path}...')
            logger.info(f'Checking root: {root}')
            logger.info(f'Checking files: {files}')
        logger.info('All files in directory correct...')
    
'''if platform == 'windows': 

    for root, dirs, files in os.walk('D:\Programming\Study\Python module 11'):
        for filename in files:
            file_path = os.path.join(root, filename)
            logger.info(f'Entering {file_path}...')
            logger.info(f'Checking root: {root}')
            logger.info(f'Checking files: {files}')
        logger.info('All files in directory correct...')'''