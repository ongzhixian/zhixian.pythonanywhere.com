################################################################################
# Define package composition
################################################################################

__all__ = ["pages", "api"]

################################################################################
# Define application imports
################################################################################

import json
import logging
from os import environ, path, makedirs
from flask import Flask, current_app
from forum_app.features.logging import log
from forum_app.features.wiki import Wiki

################################################################################
# Helper functions for Flask application definition
################################################################################

def setup_app_path():
    """Returns application root path"""

    app_path = path.dirname(path.abspath(__file__))
    
    print(f"app_path is {app_path}")
    
    return app_path


def get_app_secrets():
    """Return app_secrets from secrets (JSON) file"""

    app_secrets = {}
    
    if 'PYTHONANYWHERE_DOMAIN' in environ:
        pythonanywhere_settings_path = path.join(environ['HOME'], '.app-secrets.json')
    elif 'USERPROFILE' in environ:
        pythonanywhere_settings_path = path.join(environ['USERPROFILE'], '.pythonanywhere.json')

    with open(pythonanywhere_settings_path) as app_secrets_file:
        app_secrets = json.load(app_secrets_file)

    return app_secrets


def get_app_settings(app_path):
    """Return app_settings from app_settings.json"""

    app_settings = {}
    
    pythonanywhere_settings_path = path.join(app_path, 'app-settings.json')
    
    with open(pythonanywhere_settings_path) as app_settings_file:
        app_settings = json.load(app_settings_file)

    return app_settings


def get_logging_format(logger_name='console'):
    # Use "%(pathname)s" to figure out underlying module like so:
    # logging_format = logging.Formatter('%(levelname).3s|%(module)-12s|%(message)s -- %(pathname)s')
    # Use "%(funcName)-20s" to show which function is does log comes from:
    # logging_format = logging.Formatter('%(levelname).3s|%(module)-12s|%(funcName)-20s|%(message)s')
    logging_formats = {
        'console': logging.Formatter('%(levelname).3s|%(module)-12s|%(message)s'),
        'file': logging.Formatter('%(asctime)s|%(levelname).3s|%(module)-12s|%(message)s'),
    }

    if logger_name in logging_formats:
        return logging_formats[logger_name]

    return logging.BASIC_FORMAT
    # return logging.Formatter('%(levelname).3s|%(module)-12s|%(message)s') if logger_name == 'console' else logging.BASIC_FORMAT


def setup_file_logging(app_settings):
    try:
        if 'log_file_path' not in app_settings:
            return

        log_file_path = app_settings['log_file_path']

        # Create log file directory if it doesn't exist
        log_dir_name = path.dirname(log_file_path)
        if not path.exists(log_dir_name):
            logging.debug(f"Creating log directory {path.abspath(log_dir_name)}")
            makedirs(log_dir_name)

        file_logger = logging.FileHandler(log_file_path)
        file_logger.setFormatter(get_logging_format('file'))

        root_logger = logging.getLogger()
        root_logger.addHandler(file_logger)

    except Exception as e:
        logging.error(e)


def parse_logging_level_string(logging_level_string):
    available_logging_levels = {
        "CRITICAL": logging.CRITICAL,   # CRITICAL = 50
        "FATAL": logging.FATAL,         # FATAL = CRITICAL
        "ERROR": logging.ERROR,         # ERROR = 40
        "WARNING": logging.WARNING,     # WARNING = 30
        "WARN": logging.WARN,           # WARN = WARNING
        "INFO": logging.INFO,           # INFO = 20
        "DEBUG": logging.DEBUG,         # DEBUG = 10
        "NOTSET": logging.NOTSET        # NOTSET = 0
    }
    logging_level = logging_level_string.upper()
    
    if logging_level in available_logging_levels:
        return available_logging_levels[logging_level]

    raise ValueError(f"Invalid logging level {logging_level_string} specified.")


def apply_logging_settings(app_settings):
    try:
        if 'logging' not in app_settings:
            return

        logging_settings = app_settings['logging']

        for logger_name in logging_settings:
            try:    
                logging_level = parse_logging_level_string(logging_settings[logger_name])
                logger = logging.getLogger(logger_name)
                logger.setLevel(logging_level)
            except ValueError as ve:
                logging.warning(ve)
    except Exception as e:
        logging.error(e)


def setup_default_logging():
    try:
        console_logging_format = get_logging_format('console')
        console_logger = logging.StreamHandler()
        console_logger.setFormatter(console_logging_format)

        root_logger = logging.getLogger()
        root_logger.handlers.clear()
        root_logger.setLevel(logging.NOTSET)
        root_logger.addHandler(console_logger)
        logging.debug("Default logging configured.")
    except Exception as e:
        logging.error(e)


def configure_logging(app_settings):
    setup_default_logging()
    setup_file_logging(app_settings)
    apply_logging_settings(app_settings)
    logging.debug("Logging configured.")


################################################################################
# Define Flask application
################################################################################

app_path = setup_app_path()

app_secrets = get_app_secrets()

app_settings = get_app_settings(app_path)

configure_logging(app_settings)

log.info("Starting application.")

app = Flask(__name__, static_url_path='/', static_folder='wwwroot', template_folder='jinja')

wiki = Wiki(app_secrets['mongodb:minitools:ConnectionString'])

if "SESSION_SECRET_KEY" in app_secrets:
    app.secret_key = app_secrets["SESSION_SECRET_KEY"]


################################################################################
# Import pages and API for application
################################################################################

from forum_app.lifecycle_handlers import *
from forum_app.pages import *
from forum_app.api import *
