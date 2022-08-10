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

@app.route('/api/wms/supplier-item', methods=['GET', 'POST'])
def api_wms_supplier_item():
    breadcrumbs = [
        { 'href' : '/wms/dashboard', 'text': 'WMS' },
        { 'href' : '/wms/dashboard?menu-item=Supplier&page=2', 'text': 'Supplier' },
        { 'href' : None, 'text': 'Supplier item' },
    ]
    from forum_app.features.wms import WmsFeature
    supplier_list = WmsFeature().get_supplier_list()
    return render_template(f'wms/wms_supplier_item.html', 
        breadcrumb_list=breadcrumbs,
        data_list=supplier_list
        ), 200


@app.route('/api/wms/supplier', methods=['GET', 'POST'])
def api_wms_supplier():
    breadcrumbs = [
        { 'href' : '/wms/dashboard', 'text': 'WMS' },
        { 'href' : None, 'text': 'Supplier' }
    ]
    from forum_app.features.wms import WmsFeature
    supplier_list = WmsFeature().get_supplier_list()
    return render_template(f'wms/wms_supplier.html', 
        breadcrumb_list=breadcrumbs,
        data_list=supplier_list
        ), 200


@app.route('/api/wms/add-supplier', methods=['GET', 'POST'])
def api_wms_add_supplier():
    breadcrumbs = [
        { 'href' : '/wms/dashboard', 'text': 'WMS' },
        { 'href' : '/wms/dashboard?menu-item=Supplier&page=2', 'text': 'Supplier' },
        { 'href' : None, 'text': 'Add Supplier' },
    ]
    message = ""
    from forum_app.features.wms import WmsFeature
    supplier_list = WmsFeature().get_supplier_list()
    if request.method == 'POST':
        message = "Invalid data."
        logging.debug("api_wms_add_supplier (POST) called.")
        if 'supplier_name_field' in request.form:
            logging.debug('supplier_name_field found in request.form.')
            supplier_name = request.form['supplier_name_field']
            # Todo: add supplier to database
            from forum_app.features.wms_supplier import WmsSupplierFeature
            wms_supplier = WmsSupplierFeature()
            wms_supplier.add(supplier_name)
            message = "Supplier added."
    return render_template(f'wms/wms_add_supplier.html', 
        breadcrumb_list=breadcrumbs,
        data_list=supplier_list,
        message=message
        ), 200

# Fallback route for pages to be developed
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
        'Supplier',
        'Customer',
        'Location',
        'Invoice',
        'Credit Note',
        'Customer Data'
    ]]
    print(f"Before {module_name}")
    normalized_name = module_name.lower()
    print(f"After {module_name}")
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
    
# @app.route('/api/wms/setup-demo', methods=['GET', 'POST'])
# def api_wms_setup_demo():
#     from forum_app.features.wms import WmsFeature
#     WmsFeature().setup_demo()
#     return "OK", 200
    