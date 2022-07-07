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

from forum_app import app, app_settings, app_state

from forum_app.databases.forum_database import ForumDatabase


from forum_app.features import BaseFeatureInterface

import pdb


@app.route('/api/feature/toggle', methods=['POST'])
def api_feature_post():
    content = get_validated_toggle_content(request)
    if not content:
        return "Bad request", 400
    base_feature = BaseFeatureInterface()
    change_saved = base_feature.toggle_enable(content['feature_name'], content['is_enable'])
    if change_saved:
        enabled_message = "enabled" if content['is_enable'] else "disabled"
        return f"{content['feature_name']} {enabled_message}", 200
    else:
        return "Changes not saved", 200


def get_validated_toggle_content(request):
    """Validate content; 
    returns None if content is invalid
    returns feature_name, is_enable dictionary value if content is valid"""
    # If content is not json, its a bad request
    if not request.is_json:
        return None

    # Note: is_json just checks if the request's HTTP header Content-Type is "application/json"!
    #       It is possible to set the header as json but send form data, at which then the following request.json will break :-(
    request_content = request.json

    # # If content does not contain 'feature_name' or 'value', then its a bad request
    if 'feature_name' not in request_content or 'value' not in request_content:
        return None

    if request_content['value'] not in (True, False):
        return None

    return {
        "feature_name": request_content['feature_name'],
        "is_enable": request_content['value']
    }
