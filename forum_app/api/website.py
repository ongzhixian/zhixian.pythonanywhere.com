# 
################################################################################
# Modules and functions import statements
################################################################################

import json
import logging

from datetime import datetime
from time import time

from flask import request, make_response, abort

from flask_app import app


################################################################################
# Setup routes
# /api/datetime     -- Get server UTC datetime
# /api/epochtime    -- Get server epoch time 
# /api/test         -- Function to 
################################################################################

@app.route('/api/website/datetime', methods=['GET', 'POST'])
def api_datetime():

    logging.info("In api_datetime()")

    return str(datetime.utcnow())
