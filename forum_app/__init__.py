################################################################################
# Define package composition
################################################################################

__all__ = ["pages", "api"]

################################################################################
# Define application imports
################################################################################

import json
import logging
from flask import Flask

################################################################################
# Define application helper functions
################################################################################

def get_secrets():
    app_secrets_file = open('/home/zhixian/.app-secrets.json')
    app_secrets = json.load(app_secrets_file)
    return app_secrets



################################################################################
# Define Flask application
################################################################################

app = Flask(__name__, static_url_path='/', static_folder='wwwroot', template_folder='jinja2_templates')
secrets = get_secrets()

logging_format = logging.Formatter('%(asctime)-15s %(levelname)-8s %(funcName)-20s %(message)s')
root_logger = logging.getLogger()
# root_logger.setLevel(logging.DEBUG)
try:
    console_logger = logging.StreamHandler()
    # console_logger.setLevel(logging.ERROR)
    console_logger.setFormatter(logging_format)
    root_logger.addHandler(console_logger)
except Exception as e:
    logging.info("ERROR----------ERROR----------")
    logging.error(e)

logging.info("START-------------------------------------")
logging.info(len(root_logger.handlers))

#root_logger.handlers

#default_console_logger = root_logger.handlers[0]
#default_console_logger.setFormatter(logging_format)

################################################################################
# Import pages and API for application
################################################################################

from forum_app.pages import *
from forum_app.api import *