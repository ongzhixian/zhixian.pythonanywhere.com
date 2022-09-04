# 
################################################################################
# Modules and functions import statements
################################################################################

import json
import logging

# from os import environ, path
# from datetime import datetime
# from time import time,sleep
#from flask import render_template, redirect, url_forrequest, make_response, abort
from flask import render_template, request

from forum_app import app, app_path

from forum_app.features.ipf_portfolio import IpfPortfolioFeature

def BadRequestJsonResponse(message=None):
    return json.dumps({
        'result': 'Bad request',
        'detail': message
    }), 400

def JsonMessageResponse(message):
    return json.dumps({
        'result': message
    })

@app.route('/api/ipf/portfolio', methods=['POST'])
def api_ipf_portfolio_post():
    post_json = request.json
    if 'action' not in post_json or post_json['action'].lower() != 'add-portfolio':
        return BadRequestJsonResponse()
    portfolio_name = post_json['portfolio_name'].strip()
    if len(portfolio_name) <= 0:
        return BadRequestJsonResponse()

    ipf_portfolio = IpfPortfolioFeature()
    (rows_affected, ex) = ipf_portfolio.add_portfolio(portfolio_name)
    # Actions to add portfolio record to database
    if rows_affected > 0:
        return JsonMessageResponse("OK"), 200
    # TODO: Diagnose to provide some other detail error message; 
    #       else just leave blank
    return BadRequestJsonResponse()
    