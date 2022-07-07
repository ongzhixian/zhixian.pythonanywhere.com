################################################################################
# Define package composition
################################################################################

__all__ = ["pages", "api"]

################################################################################
# Define application imports
################################################################################

import json
import logging
from mimetypes import init
from os import environ, path
from importlib import import_module
from inspect import getmembers, isclass
from flask import Flask, current_app

import pdb


################################################################################
# Define application helper functions
################################################################################

# def cache(key, value=None):
#     if value is not None:
#         cache.items[key] = value
#     return cache.items[key] if key in cache.items else None

# cache.items = {}

# def app_state(key, value=None):
#     if value is not None:
#         app_state.items[key] = value
#     return app_state.items[key] if key in app_state.items else None

# app_state.items = {}



# def get_feature_instance_list():
#     feature_instance_list = []    
#     import importlib, inspect
#     from forum_app.features import __all__ as feature_list, BaseFeatureInterface
#     for feature in feature_list:
#         feature_module = importlib.import_module(f"forum_app.features.{feature}")
#         class_member_list = inspect.getmembers(feature_module, inspect.isclass)
#         for class_member in class_member_list:
#             feature_class = class_member[1]
#             is_feature = issubclass(feature_class, BaseFeatureInterface)
#             if is_feature:
#                 feature_instance = feature_class()
#                 feature_instance_list.append(feature_instance)
#     return feature_instance_list

# def get_features_map():
#     map = {}
#     import importlib, inspect
#     from forum_app.features import __all__ as feature_list, BaseFeatureInterface
#     for feature in feature_list:
#         feature_module = importlib.import_module(f"forum_app.features.{feature}")
#         class_member_list = inspect.getmembers(feature_module, inspect.isclass)
#         for class_member in class_member_list:
#             feature_class = class_member[1]
#             is_feature = issubclass(feature_class, BaseFeatureInterface)
#             if is_feature:
#                 feature_instance = feature_class()
#                 if feature_instance.feature_name is None or feature_instance.feature_name in map:
#                     continue
#                 map[feature_instance.feature_name] = feature_instance
#     return map



# def load_feature_settings(app_settings):
#     feature_instance_list = get_feature_instance_list()
#     for feature_instance in feature_instance_list:
#         feature_instance.load_app_settings(app_settings)
#     return app_settings









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


# event_callbacks = {}
# def subscribe_to_event(event_name, callback):
#     if event_name not in event_callbacks:
#         event_callbacks[event_name] = []
    

# def discovery_phase():
#     pass



## re-worked

def setup_app_path():
    """Returns application root path"""
    # PythonAnywhere note: `os.getcwd()` will point to the working directory 
    # app_path = os.path.join(os.getcwd(), 'forum_app')
    app_path = path.dirname(path.abspath(__file__))
    print(f"app_path is {app_path}")
    return app_path


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
    
    return logging.Formatter('%(levelname).3s|%(module)-12s|%(message)s') if logger_name == 'console' else logging.BASIC_FORMAT

def setup_default_logging():
    try:
        console_logging_format = get_logging_format('console')
        console_logger = logging.StreamHandler()
        console_logger.setFormatter(console_logging_format)

        # for h in root_logger.handlers:
        #     logging.info(str(h))
        #     # logging.info(str(h.level))
        #     # logging.info(str(h.name))

        root_logger = logging.getLogger()
        root_logger.setLevel(logging.NOTSET)
        root_logger.addHandler(console_logger)
        logging.debug("Default logging configured.")
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

def configure_logging(app_settings):
    setup_default_logging()
    apply_logging_settings(app_settings)
    logging.debug("Logging configured.")


def get_app_secrets():
    app_secrets = {}
    if 'PYTHONANYWHERE_DOMAIN' in environ:
        pythonanywhere_settings_path = path.join(environ['HOME'], '.app-secrets.json')
    elif 'USERPROFILE' in environ:
        pythonanywhere_settings_path = path.join(environ['USERPROFILE'], '.pythonanywhere.json')

    with open(pythonanywhere_settings_path) as app_secrets_file:
        app_secrets = json.load(app_secrets_file)
    return app_secrets


def is_database_class(member_object):
    from forum_app.databases import BaseDatabaseInterface
    return isclass(member_object) and issubclass(member_object, BaseDatabaseInterface) and member_object is not BaseDatabaseInterface
    
def discover_database_classes():
    database_class_map = {}
    from forum_app.databases import __all__ as database_name_list
    for database_name in database_name_list:
        database_module = import_module(f"forum_app.databases.{database_name}")
        module_database_list = getmembers(database_module, predicate=is_database_class)
        for module_database in module_database_list:
            database_class_map[module_database[0]] = module_database[1]
    return database_class_map

def initialize_databases():
    database_class_map = discover_database_classes()
    for database_class_name in database_class_map:
        database_instance = database_class_map[database_class_name]()
        database_instance.create_database_if_not_exists()
        database_instance.is_missing_key_tables()
    logging.debug("Databases initialized.")
    return database_class_map


def is_feature_class(member_object):
    from forum_app.features import BaseFeatureInterface
    return isclass(member_object) and issubclass(member_object, BaseFeatureInterface) and member_object is not BaseFeatureInterface


def discover_feature_classes():
    feature_class_map = {}
    from forum_app.features import __all__ as feature_list
    for feature in feature_list:
        feature_module = import_module(f"forum_app.features.{feature}")
        module_feature_list = getmembers(feature_module, predicate=is_feature_class)
        for module_feature in module_feature_list:
            feature_class_map[module_feature[0]] = module_feature[1]
    return feature_class_map

def initialize_features():
    feature_class_map = discover_feature_classes()
    for feature_class_name in feature_class_map:
        feature_instance = feature_class_map[feature_class_name]()
        feature_instance.initialize()
    logging.debug("Features initialized.")
    return feature_class_map


def setup_drawer_sitemap_menu():
    return [
        ("Sitemap item", "/sample/sitemap-item", "table_rows")
    ]

def setup_drawer_admin_menu():
    return [
        # ("Admin item", "/sample/admin-item", "table_rows")
    ]

def setup_header_menu():
    return [
        ("Header item", "/sample/header-item", "table_rows")
    ]

def initialize_app_state():
    app_state = {}
    app_state['feature'] = {}
    app_state['drawer_sitemap_menu'] = setup_drawer_sitemap_menu()
    app_state['drawer_admin_menu'] = setup_drawer_admin_menu()
    app_state['header_menu'] = setup_header_menu()
    return app_state
    

################################################################################
# Define Flask application
################################################################################

app_path = setup_app_path()

app_secrets = get_app_secrets()

app_settings = get_app_settings(app_path)

app_state = initialize_app_state()

configure_logging(app_settings)

database_class_map = initialize_databases()

feature_class_map = initialize_features()

# app_settings = load_feature_settings(app_settings)
# app_state('feature_map', get_features_map())

logging.info("Starting application.")

app = Flask(__name__, static_url_path='/', static_folder='wwwroot', template_folder='jinja2_templates')


# menu_items = [
#     ("Inv 111", "/inv/dashboard", "table_rows"),
#     ("Inv 222", "/inv/dashboard", "table_rows"),
# ]

# with app.app_context():
#     current_app.feature_instance_list = menu_items

# if "SESSION_SECRET_KEY" in secrets:
#     app.secret_key = secrets["SESSION_SECRET_KEY"]


################################################################################
# Import pages and API for application
################################################################################

from forum_app.lifecycle_handlers import *
from forum_app.pages import *
from forum_app.api import *
