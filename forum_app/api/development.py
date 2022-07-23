# 
################################################################################
# Modules and functions import statements
################################################################################

import enum
import json
import logging

from os import environ
from datetime import datetime
from time import time

from flask import request, make_response, abort

from forum_app import app
from forum_app.databases.forum_database import ForumDatabase
from forum_app.features.development_note import DevelopmentNoteFeature

# from enum import Enum
# class ResponseStatus(Enum):
#     OK = 1

def json_response(obj, status):
    pass
    # return json.dumps({
    #     'type': 'error',
    #     'text': error
    # })


@app.route('/api/development/note', methods=['POST'])
def api_development_note_post():
    if not request.is_json:
        return json.dumps({})

    logging.debug(request.json)
    
    feature = DevelopmentNoteFeature()
    (row_count, error) = feature.add_note(request.json)
    
    if error is not None:
        return json.dumps({
            'type': 'error',
            'text': error
        })
    
    if row_count <= 0:
        return json.dumps({
            'type': 'fail',
            'text': 'Fail to save note.'
        })
    
    return json.dumps({
        'type': 'done',
        'text': "Note saved."
    })

    