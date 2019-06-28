"""Example application settings
rename this to settings
"""
import os
import sys
import logging

#set path for resources
DIRNAME = os.path.dirname(__file__)
RESOURCEPATH = os.path.join(DIRNAME, 'resources/')
sys.path.append(RESOURCEPATH)
#set path for DB
DBPATH = os.path.join(DIRNAME, 'database/')
sys.path.append(DBPATH)

#configure logger
LOG_PATH = "./storage/logs/"
LOG_NAME = "app.log"
LOG_FILE = LOG_PATH+LOG_NAME
LOGGER = logging.getLogger()
logging.basicConfig(
    filename=LOG_FILE,
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
    "port": "32815",
    "LOGGER": LOGGER
}

#configure email
EMAIL_FROM = "admin@example.com"
EMAIL_TO = "admin@example.com"
EMAIL_PWORD = ""
EMAIL_HOST_SERVER = "smtp.gmail.com"
EMAIL_PORT = 465
