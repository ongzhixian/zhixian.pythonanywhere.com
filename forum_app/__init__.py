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
from stat import FILE_ATTRIBUTE_OFFLINE
from flask import Flask, current_app

import pdb


################################################################################
# Define application helper functions
################################################################################

def cache(key, value=None):
    if value is not None:
        cache.items[key] = value
    return cache.items[key] if key in cache.items else None

cache.items = {}

def app_state(key, value=None):
    if value is not None:
        app_state.items[key] = value
    return app_state.items[key] if key in app_state.items else None

app_state.items = {}

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
    for k, v in sorted(os.environ.items()):
        print(k+':', v)
        print('\n')

    app_settings = {}
    pythonanywhere_settings_path = os.path.join(app_path, 'app-settings.json')
    with open(pythonanywhere_settings_path) as app_settings_file:
        app_settings = json.load(app_settings_file)
    return app_settings


def setup_app_path():
    # /home/zhixian/website/run/forum_app/data/database_init_scripts
    #         D:\src\github\any\forum_app\data\database_init_scripts
    # if 'PYTHONANYWHERE_DOMAIN' in os.environ:
    #     return '/home/zhixian/website/forum_app'
    # elif 'USERPROFILE' in os.environ:
    app_path = os.path.join(os.getcwd(), 'forum_app')
    print(f"app_path is {app_path}")
    alt_app_path = os.path.dirname(os.path.abspath(__file__))
    print(f"alt_app_path is {alt_app_path}")
    return app_path

def get_feature_instance_list():
    feature_instance_list = []    
    import importlib, inspect
    from forum_app.features import __all__ as feature_list, BaseFeatureInterface
    for feature in feature_list:
        feature_module = importlib.import_module(f"forum_app.features.{feature}")
        class_member_list = inspect.getmembers(feature_module, inspect.isclass)
        for class_member in class_member_list:
            feature_class = class_member[1]
            is_feature = issubclass(feature_class, BaseFeatureInterface)
            if is_feature:
                feature_instance = feature_class()
                feature_instance_list.append(feature_instance)
    return feature_instance_list

def get_features_map():
    map = {}
    import importlib, inspect
    from forum_app.features import __all__ as feature_list, BaseFeatureInterface
    for feature in feature_list:
        feature_module = importlib.import_module(f"forum_app.features.{feature}")
        class_member_list = inspect.getmembers(feature_module, inspect.isclass)
        for class_member in class_member_list:
            feature_class = class_member[1]
            is_feature = issubclass(feature_class, BaseFeatureInterface)
            if is_feature:
                feature_instance = feature_class()
                if feature_instance.feature_name is None or feature_instance.feature_name in map:
                    continue
                map[feature_instance.feature_name] = feature_instance
    return map



def load_feature_settings(app_settings):
    feature_instance_list = get_feature_instance_list()
    for feature_instance in feature_instance_list:
        feature_instance.load_app_settings(app_settings)
    return app_settings

def initialize_databases():
    import importlib, inspect
    from forum_app.databases import __all__ as database_name_list, BaseDatabaseInterface
    for database_name in database_name_list:
        database_module = importlib.import_module(f"forum_app.databases.{database_name}")
        database_class_list = inspect.getmembers(database_module, inspect.isclass)
        for database_class_member in database_class_list:
            database_class = database_class_member[1]
            is_database = issubclass(database_class, BaseDatabaseInterface)
            if is_database:
                database_instance = database_class()
                database_instance.create_database_if_not_exists()
                database_instance.is_missing_key_tables()


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


def setup_default_logging():
    try:
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
        logging.debug("Default logging configured.")
    except Exception as e:
        logging.error(e)

def configure_logging(app_settings):
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
    except Exception as e:
        logging.error(e)


# def checkup():
#     # Application should have minimally 2 tables
#     # 1.    _db_migrate
#     # 2.    _feature
#     import importlib, inspect
#     from forum_app.databases import __all__ as database_name_list, BaseDatabaseInterface
#     for database_name in database_name_list:
#         database_module = importlib.import_module(f"forum_app.databases.{database_name}")
#         database_class_list = inspect.getmembers(database_module, inspect.isclass)
#         for database_class_member in database_class_list:
#             database_class = database_class_member[1]
#             is_database = issubclass(database_class, BaseDatabaseInterface)
#             if is_database:
#                 database_instance = database_class()
#                 database_instance.ensure()


event_callbacks = {}
def subscribe_to_event(event_name, callback):
    if event_name not in event_callbacks:
        event_callbacks[event_name] = []
    

def discovery_phase():
    pass


################################################################################
# Define Flask application
################################################################################

app_path = setup_app_path()

app_settings = get_app_settings(app_path)

setup_default_logging()


secrets = get_secrets()
# initialize_databases()
# app_settings = load_feature_settings(app_settings)
# app_state('feature_map', get_features_map())
# configure_logging(app_settings)

logging.info("[APPLICATION START]")

app = Flask(__name__, static_url_path='/', static_folder='wwwroot', template_folder='jinja2_templates')

menu_items = [
    ("Inv 111", "/inv/dashboard", "table_rows"),
    ("Inv 222", "/inv/dashboard", "table_rows"),
]

with app.app_context():
    current_app.feature_instance_list = menu_items

# if "SESSION_SECRET_KEY" in secrets:
#     app.secret_key = secrets["SESSION_SECRET_KEY"]


################################################################################
# Import pages and API for application
################################################################################

from forum_app.lifecycle_handlers import *
from forum_app.pages import *
from forum_app.api import *
