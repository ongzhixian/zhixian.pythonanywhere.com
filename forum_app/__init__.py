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


def get_app_settings(app_path):
    app_settings = {}
    pythonanywhere_settings_path = os.path.join(app_path, 'app-settings.json')
    with open(pythonanywhere_settings_path) as app_settings_file:
        app_settings = json.load(app_settings_file)
    return app_settings


def parse_logging_level_string(logging_level_string):
    # CRITICAL = 50
    # FATAL = CRITICAL
    # ERROR = 40
    # WARNING = 30
    # WARN = WARNING
    # INFO = 20
    # DEBUG = 10
    # NOTSET = 0
    available_logging_levels = {
        "CRITICAL": logging.CRITICAL,
        "FATAL": logging.FATAL,
        "ERROR": logging.ERROR,
        "WARNING": logging.WARNING,
        "WARN": logging.WARN,
        "INFO": logging.INFO,
        "DEBUG": logging.DEBUG,
        "NOTSET": logging.NOTSET
    }
    logging_level = logging_level_string.upper()
    
    if logging_level in available_logging_levels:
        return available_logging_levels[logging_level]

    raise ValueError(f"Invalid logging level {logging_level_string} specified.")

def setup_logging(app_settings):
    try:
        if 'logging' in app_settings:
            logging_settings = app_settings['logging']
            for logger_name in logging_settings:
                try:    
                    logging_level = parse_logging_level_string(logging_settings[logger_name])
                    logger = logging.getLogger(logger_name)
                    logger.setLevel(logging_level)
                except ValueError as ve:
                    logging.warning(ve)

        # Use "%(pathname)s" to figure out underlying module
        # logging_format = logging.Formatter('%(levelname).3s|%(module)-12s|%(message)s -- %(pathname)s')
        # Logging with function name
        # logging_format = logging.Formatter('%(levelname).3s|%(module)-12s|%(funcName)-20s|%(message)s')
        
        logging_format = logging.Formatter('%(levelname).3s|%(module)-12s|%(message)s')
        root_logger = logging.getLogger()
        root_logger.setLevel(logging.NOTSET)
        console_logger = logging.StreamHandler()
        console_logger.setFormatter(logging_format)
        root_logger.addHandler(console_logger)
    except Exception as e:
        logging.error(e)


def setup_app_path():
    # /home/zhixian/website/run/forum_app/data/database_init_scripts
    #         D:\src\github\any\forum_app\data\database_init_scripts
    if 'PYTHONANYWHERE_DOMAIN' in os.environ:
        return '/home/zhixian/website/forum_app'
    elif 'USERPROFILE' in os.environ:
        return os.path.join(os.getcwd(), 'forum_app')


################################################################################
# Define Flask application
################################################################################

app = Flask(__name__, static_url_path='/', static_folder='wwwroot', template_folder='jinja2_templates')

app_path = setup_app_path()

secrets = get_secrets()

app_settings = get_app_settings(app_path)

if "SESSION_SECRET_KEY" in secrets:
    app.secret_key = secrets["SESSION_SECRET_KEY"]

setup_logging(app_settings)

logging.info("[APPLICATION START]")

################################################################################
# Import pages and API for application
################################################################################

from forum_app.lifecycle_handlers import *
from forum_app.pages import *
from forum_app.api import *
