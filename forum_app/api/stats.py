# 
################################################################################
# Modules and functions import statements
################################################################################

import json
import logging

from os import environ
from datetime import datetime, date
from time import time

from flask import request, make_response, abort

from forum_app import app, secrets
from forum_app.modules.forum_db import ForumDb

def defaultConverter(o):
    # import pdb
    # pdb.set_trace()
    if isinstance(o, datetime):
        return o.__str__()
    if isinstance(o, date):
        return str(o)

@app.route('/api/stats/weblink', methods=['GET', 'POST'])
def api_stats_weblink_post():
    mydb = ForumDb()
    rec = mydb.get_links_added_by_date()
    logging.info("In api_weblink_post()")
    return json.dumps(rec, default = defaultConverter), 200
    