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

from forum_app import app, secrets
from forum_app.modules.forum_db import ForumDb



@app.route('/api/stats', methods=['GET', 'POST'])
def api_stats_post():
    # If content is not json, its a bad request
    if not request.is_json:
        return "Bad request", 400
    
    content = request.json
    # If content is not a list of strings, its a bad request
    if type(content) is not list:
        return "Bad request", 400
    
    mydb = ForumDb()
    data = []

    count = 0
    for url in content:
        data.append((url, ))
        count = count + 1

    print("data len is", len(data))
    mydb.add_weblinks(data)

    logging.info("In api_weblink_post()")
    return f"{count} links processed", 201
    