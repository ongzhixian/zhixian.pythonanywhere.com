# 
################################################################################
# Modules and functions import statements
################################################################################

import json
import logging

import hmac
import hashlib

from datetime import datetime
from time import time

from flask import request, make_response, abort

from forum_app import app, secrets

import git
import os

@app.route('/api/website/env', methods=['GET', 'POST'])
def api_website_env():

    logging.info("In api_website_env()")

    # sec1 = os.getenv('BASH_SECRET')
    # sec2 = os.getenv('OTHER_SECRET')

    # app_secrets_file = open('/home/zhixian/.app-secrets.json')
    # app_secrets = json.load(app_secrets_file)
    # return str(app_secrets)
    return secrets['GIT_SECRET']

    # return str(os.environ)
    #return str(sec1) + ' -- ' + str(sec2)


@app.route('/api/website/datetime', methods=['GET', 'POST'])
def api_datetime():

    logging.info("In api_datetime()")

    return str(datetime.utcnow())


@app.route('/api/website/change-notification', methods=['POST'])
def api_website_change_notification():

    logging.info("In api_website_change_notification()")
    logging.info(str(request.headers))



    if request.method == 'POST' and "X-Hub-Signature" in request.headers and 'GIT_SECRET' in secrets:
        signature = request.headers["X-Hub-Signature"]
        encoded_git_hook_secret = secrets['GIT_SECRET'].encode("utf8")
        github_hash_key, github_hash = signature.split("=")

        logging.info(f"github_hash_key:{github_hash_key}, github_hash:{github_hash}")

        mac = hmac.new(encoded_git_hook_secret, msg=request.data, digestmod=github_hash_key)
        mac_hex_digest = mac.hexdigest()
        logging.info(f"Mac: {mac_hex_digest}")
        
        is_valid = hmac.compare_digest(mac.hexdigest(), github_hash)
        logging.info(f"is_valid: {is_valid}")

    if request.method == 'POST':
        repo = git.Repo('/home/zhixian/website')
        origin = repo.remotes.origin
        origin.pull()
        return 'Updated PythonAnywhere successfully', 200
    else:
        return 'Wrong event type', 400
