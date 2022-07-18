# 
################################################################################
# Modules and functions import statements
################################################################################

import json
import logging

from os import environ
from datetime import datetime
from time import time

from flask import request, make_response, abort

from forum_app import app
from forum_app.databases.forum_database import ForumDatabase



@app.route('/api/instrument/search', methods=['POST'])
def api_instrument_search():
    data = {
        "Apple": None,
        "Microsoft": None,
        "Google": 'https://placehold.it/250x250'
    }

    return json.dumps(data)
