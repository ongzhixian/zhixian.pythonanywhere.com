################################################################################
# Define package composition
################################################################################

__all__ = ["pages", "api"]

################################################################################
# Define Flask application
################################################################################

from flask import Flask

app = Flask(__name__, static_url_path='/', static_folder='wwwroot', template_folder='jinja2_templates')

################################################################################
# Import pages and API for application
################################################################################

from forum_app.pages import *
from forum_app.api import *