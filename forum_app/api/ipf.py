# 
################################################################################
# Modules and functions import statements
################################################################################

import json
import logging
import urllib.request

# from os import environ, path
# from datetime import datetime
# from time import time,sleep
#from flask import render_template, redirect, url_forrequest, make_response, abort
from flask import render_template, request

from forum_app import app, app_path

@app.route('/api/ipf/test', methods=['GET', 'POST'])
def api_ipf_test():
    api_url = "https://query1.finance.yahoo.com/v8/finance/chart/BN4.SI"
    request = urllib.request.Request(api_url)
    with urllib.request.urlopen(request) as response:
        json_data = json.loads(response.read().decode("utf-8"))
    chart_json = json_data['chart']
    result = chart_json['result'][0]
    meta = chart_json['result'][0]['meta']
    timestamp = chart_json['result'][0]['timestamp']
    indicators = chart_json['result'][0]['indicators']
    breakpoint()
    return "OK", 200
    
    # https://query2.finance.yahoo.com/v7/finance/quote?symbols=BN4.SI&fields=exchangeTimezoneName,exchangeTimezoneShortName,regularMarketTime,gmtOffSetMilliseconds&region=US&lang=en-US
    # https://query1.finance.yahoo.com/v8/finance/chart/BN4.SI?region=US&lang=en-US&includePrePost=false&interval=1mo&useYfid=true&range=max&corsDomain=finance.yahoo.com&.tsrc=finance

    # return render_template(f'wms/wms_supplier_item.html', 
    #     breadcrumb_list=breadcrumbs,
    #     data_list=supplier_list
    #     ), 200
