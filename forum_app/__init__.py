################################################################################
# Define package composition
################################################################################

__all__ = ["pages", "api"]

################################################################################
# Define application imports
################################################################################

import json
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

################################################################################
# Import pages and API for application
################################################################################

from forum_app.pages import *
from forum_app.api import *