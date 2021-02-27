# 
################################################################################
# Modules and functions import statements
################################################################################

import json
import logging

from datetime import datetime
from time import time

from flask import request, make_response, abort

from forum_app import app

import git
import os

@app.route('/api/website/env', methods=['GET', 'POST'])
def api_website_env():

    logging.info("In api_website_env()")

    sec1 = os.getenv('BASH_SECRET')
    sec2 = os.getenv('OTHER_SECRET')

    return str(sec1) + ' -- ' + str(sec2)


@app.route('/api/website/datetime', methods=['GET', 'POST'])
def api_datetime():

    logging.info("In api_datetime()")

    return str(datetime.utcnow())


@app.route('/api/website/change-notification', methods=['POST'])
def api_website_change_notification():

    logging.info("In api_website_change_notification()")

    if request.method == 'POST':
        repo = git.Repo('/home/zhixian/website')
        origin = repo.remotes.origin
        origin.pull()
        return 'Updated PythonAnywhere successfully', 200
    else:
        return 'Wrong event type', 400
