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

from forum_app import app, app_secrets

import git
import os

@app.route('/api/website/env', methods=['GET', 'POST'])
def api_website_env():
    try:
        response_message = f"UTC date-time is {datetime.utcnow()}"
        logging.info(response_message)
        return response_message
    except Exception as e:
        logging.info("ERROR----------ERROR----------")
        logging.error(e)


@app.route('/api/website/datetime', methods=['GET', 'POST'])
def api_datetime():
    """Simple api that returns server's UTC datetime"""
    try:
        response_message = f"UTC date-time is {datetime.utcnow()}"
        logging.info(response_message)
        return response_message
    except Exception as e:
        logging.info("ERROR----------ERROR----------")
        logging.error(e)


@app.route('/api/website/change-notification', methods=['POST'])
def api_website_change_notification():
    """This is github webhook endpoint"""

    logging.info("In api_website_change_notification()")

    is_post = request.method == 'POST'
    has_x_hub_signature = "X-Hub-Signature" in request.headers
    has_git_webhook_secret = 'GIT_WEBHOOK_SECRET' in app_secrets

    if is_post and has_x_hub_signature and has_git_webhook_secret:
        signature = request.headers["X-Hub-Signature"]
        encoded_git_webhook_secret = app_secrets['GIT_WEBHOOK_SECRET'].encode("utf8")
        hash_algorithm, hash_value = signature.split("=")

        logging.info(f"github_hash_key:{hash_algorithm}, github_hash:{hash_value}")

        mac = hmac.new(encoded_git_webhook_secret, msg=request.data, digestmod=hash_algorithm)
        is_matching_hash = hmac.compare_digest(mac.hexdigest(), hash_value)
        logging.info(f"Github hash match: {is_matching_hash}")

        if is_matching_hash:
            repo = git.Repo('/home/zhixian/website')
            origin = repo.remotes.origin
            origin.pull()

            logging.info("Local Github repository pulled.")
            return 'OK', 200
    else:
        error_message = f"Invalid api_website_change_notification() call; is_post:{is_post}, has_x_hub_signature: {has_x_hub_signature} has_git_webhook_secret: {has_git_webhook_secret}"
        logging.info(error_message)
        return error_message, 400
