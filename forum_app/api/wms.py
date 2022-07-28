# 
################################################################################
# Modules and functions import statements
################################################################################

# import json
# import logging

# from os import environ, path
# from datetime import datetime
# from time import time,sleep
#from flask import render_template, redirect, url_forrequest, make_response, abort
from flask import render_template

from forum_app import app, app_path
# from forum_app.databases.forum_database import ForumDatabase

@app.route('/api/wms/<module_name>', methods=['GET', 'POST'])
def api_wms_module(module_name):
    all_modules = [x.lower() for x in [
        'Receiving',
        'Received',
        'Sending',
        'Picking',
        'Packing',
        'Sent',
        'Item_Data',
        'Supplier_Data',
        'Customer_Data',
        'Location_Data',
        'Invoice',
        'Credit Note',
        'Customer Data'
    ]]
    module_name = module_name.lower()
    if module_name in all_modules:
        # print(f'wms/wms_{module_name}.html')
        # print(render_template(f'wms/wms_{module_name}.html'))
        breadcrumbs = [
            { 'href' : '/wms/dashboard', 'text': 'WMS' },
            { 'href' : None, 'text': module_name }
        ]
        return render_template(f'wms/wms_{module_name}.html', breadcrumb_list=breadcrumbs), 200
    return f"""<p>Placeholder for {module_name}</p>""", 200
    # module_html_templates = {
    #     "receiving": 'wms/wms_receiving.html',
    #     "received": 'wms/wms_received.html'
    # }
    # if module_name in module_html_templates:    
    #     html = render_template(module_html_templates[module_name])
    # else:
    #     html = f"""<p>Placeholder for {module_name}</p>"""
    
    