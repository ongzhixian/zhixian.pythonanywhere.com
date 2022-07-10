# 
################################################################################
# Modules and functions import statements
################################################################################

import logging
from flask import request
from forum_app import app
from forum_app.features import BaseFeatureInterface
import pdb

@app.route('/api/feature/toggle', methods=['POST'])
def api_feature_post():
    """This allows user to toggle feature flags from UI.

    **Discouraged usage**

    But UI changes are not update (when there are UI changes),
    (user has to refresh page manually to see changes).
    Favouring a post-back approach for now, until UI 
    is changed to use something else (webhooks, websockets or better)
    """
    response_message = "Changes not saved"
    content = get_validated_toggle_content(request)
    if not content:
        return "Bad request", 400
    # logging.info(f"content {content}")

    base_feature = BaseFeatureInterface()
    change_saved = base_feature.toggle_enable(content['feature_name'], content['is_enable'])
    if change_saved:
        enabled_message = "enabled" if content['is_enable'] else "disabled"
        response_message = f"{content['feature_name']} {enabled_message}"
    logging.info(response_message)
    return response_message, 200


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
