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

    logging.info("In api_website_env()")

    # sec1 = os.getenv('BASH_SECRET')
    # sec2 = os.getenv('OTHER_SECRET')

    # app_secrets_file = open('/home/zhixian/.app-secrets.json')
    # app_secrets = json.load(app_secrets_file)
    # return str(app_secrets)
    return app_secrets['GIT_SECRET']

    # return str(os.environ)
    #return str(sec1) + ' -- ' + str(sec2)


@app.route('/api/website/datetime', methods=['GET', 'POST'])
def api_datetime():
    logging.info("In api_datetime()")
    # root_logger = logging.getLogger()
    try:
        # logging.info(len(root_logger.handlers))

        # logging.info((str(root_logger.handlers[0])))
        # logging.info((str(root_logger.handlers[1])))

        # for h in root_logger.handlers:
        #     logging.info(str(h))
        #     # logging.info(str(h.level))
        #     # logging.info(str(h.name))
        
        # logging_format = logging.Formatter('%(asctime)-15s %(levelname)-8s %(funcName)-20s %(message)s')
        # default_console_logger = root_logger.handlers[0]
        # default_console_logger.setFormatter(logging_format)

        # logging.info("OK SZET")

        # x = root_logger.handlers[0]
        # logging.info(x.name)
        # logging.info(x.level)
        # logging.info(str(type(x)))
        # x.setFormatter(logging_format)

        # y = root_logger.handlers[1]
        # logging.info(y.name)
        # logging.info(y.level)
        # logging.info(str(type(y)))
        # y.setFormatter(logging_format)

        logging.info('asdzxc')

        #logging.info(str(dir(logging.getLogger().handlers[0])))

        # logging.info(str(logging.getLogger().handlers[0]))
        # logging.info(str(logging.getLogger().handlers[1]))

        # logging.info(root_logger.handlers[0].name)
        # logging.info(root_logger.handlers[1].name)
        # logging.info(root_logger.handlers[0].level)
        # logging.info(root_logger.handlers[1].level)
    except Exception as e:
        logging.info("ERROR----------ERROR----------")
        logging.error(e)

    logging.info("In api_datetime() END")
    return str(datetime.utcnow())


@app.route('/api/website/change-notification', methods=['POST'])
def api_website_change_notification():

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
