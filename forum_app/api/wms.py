# 
################################################################################
# Modules and functions import statements
################################################################################

# import json
import logging

# from os import environ, path
# from datetime import datetime
# from time import time,sleep
#from flask import render_template, redirect, url_forrequest, make_response, abort
from flask import render_template, request

from forum_app import app, app_path
# from forum_app.databases.forum_database import ForumDatabase

@app.route('/api/wms/Suppliers', methods=['GET', 'POST'])
def api_wms_suppliers():
    breadcrumbs = [
        { 'href' : '/wms/dashboard', 'text': 'WMS' },
        { 'href' : None, 'text': 'Suppliers' }
    ]
    from forum_app.features.wms import WmsFeature
    supplier_list = WmsFeature().get_supplier_list()
    print(len(supplier_list))
    return render_template(f'wms/wms_suppliers.html', 
        breadcrumb_list=breadcrumbs,
        data_list=supplier_list
        ), 200


@app.route('/api/wms/add-supplier', methods=['GET', 'POST'])
def api_wms_add_supplier():
    breadcrumbs = [
        { 'href' : '/wms/dashboard', 'text': 'WMS' },
        { 'href' : None, 'text': 'Suppliers' }
    ]
    from forum_app.features.wms import WmsFeature
    supplier_list = WmsFeature().get_supplier_list()
    if request.method == 'POST':
        logging.debug("api_wms_add_supplier (POST) called.")
        if 'supplier_name_field' in request.form:
            logging.debug('supplier_name_field found in request.form.')
            supplier_name = request.form['supplier_name_field']
            # Todo: add supplier to database
        else:
            logging.debug('supplier_name_field missing in request.form.')
        breakpoint()
    return render_template(f'wms/wms_add_supplier.html', 
        breadcrumb_list=breadcrumbs,
        data_list=supplier_list
        ), 200


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
        'Suppliers',
        'Customer',
        'Location',
        'Invoice',
        'Credit Note',
        'Customer Data'
    ]]
    normalized_name = module_name.lower()
    if normalized_name in all_modules:
        # print(f'wms/wms_{module_name}.html')
        # print(render_template(f'wms/wms_{module_name}.html'))
        breadcrumbs = [
            { 'href' : '/wms/dashboard', 'text': 'WMS' },
            { 'href' : None, 'text': module_name }
        ]
        return render_template(f'wms/wms_{normalized_name}.html', breadcrumb_list=breadcrumbs), 200
    return f"""<p>Placeholder for {module_name}</p>""", 200
    # module_html_templates = {
    #     "receiving": 'wms/wms_receiving.html',
    #     "received": 'wms/wms_received.html'
    # }
    # if module_name in module_html_templates:    
    #     html = render_template(module_html_templates[module_name])
    # else:
    #     html = f"""<p>Placeholder for {module_name}</p>"""
    
@app.route('/api/wms/setup-demo', methods=['GET', 'POST'])
def api_wms_setup_demo():
    from forum_app.features.wms import WmsFeature
    WmsFeature().setup_demo()
    return "OK", 200
    