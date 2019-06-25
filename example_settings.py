"""Example application settings
rename this to settings
"""
import os
import sys
import logging

#set paths for resources
DIRNAME = os.path.dirname(__file__)
RESOURCEPATH = os.path.join(DIRNAME, 'resources/')
sys.path.append(RESOURCEPATH)
#set paths for DB
DBPATH = os.path.join(DIRNAME, 'database/')
sys.path.append(DBPATH)

#configure logger
LOG_PATH = "./storage/logs/"
LOG_NAME = "app.log"
LOGGER = logging.getLogger()
logging.basicConfig(
    filename=LOG_PATH+LOG_NAME,
    filemode='w',
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%m/%d/%Y %I:%M:%S %p',
    level=logging.DEBUG
)

#configure DB
DB_CONN = {
    "database": "lamp",
    "user": "postgres",
    "password": "",
    "host": "127.0.0.1",
    "port": "33158"
}
