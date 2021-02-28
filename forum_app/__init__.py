################################################################################
# Define package composition
################################################################################

__all__ = ["pages", "api"]

################################################################################
# Define application imports
################################################################################

import json
import logging
import os
from flask import Flask

################################################################################
# Define application helper functions
################################################################################

def get_secrets():
    app_secrets = {}
    if 'PYTHONANYWHERE_DOMAIN' in os.environ:
        pythonanywhere_settings_path = '/home/zhixian/.app-secrets.json'
    elif 'USERPROFILE' in os.environ:
        pythonanywhere_settings_path = os.path.join(os.environ['USERPROFILE'], '.pythonanywhere.json')
    
    with open(pythonanywhere_settings_path) as app_secrets_file:
        app_secrets = json.load(app_secrets_file)
    return app_secrets


def setup_logging():
    try:
        logging_format = logging.Formatter('[%(levelname)-8s] %(funcName)-20s %(message)s')
        root_logger = logging.getLogger()
        root_logger.setLevel(logging.NOTSET)
        console_logger = logging.StreamHandler()
        console_logger.setFormatter(logging_format)
        root_logger.addHandler(console_logger)
    except Exception as e:
        logging.error(e)


################################################################################
# Define Flask application
################################################################################

app = Flask(__name__, static_url_path='/', static_folder='wwwroot', template_folder='jinja2_templates')
secrets = get_secrets()
setup_logging()
logging.info("[APPLICATION START]")


################################################################################
# Import pages and API for application
################################################################################

from forum_app.pages import *
from forum_app.api import *