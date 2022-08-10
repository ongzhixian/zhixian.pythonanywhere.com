# 
################################################################################
# Modules and functions import statements
################################################################################

import logging
import json
from flask import render_template, request

from forum_app import app, app_path
from forum_app.features.wms_location import WmsLocationFeature
from forum_app.features.wms_location_type import WmsLocationTypeFeature


@app.route('/api/wms/location-type', methods=['GET', 'POST'])
def api_wms_location_type():
    wms_location_type = WmsLocationTypeFeature()
    try:
        post_data = request.json
    except Exception as ex:
        logging.error(f"Bad request {ex}")
        return f"Bad request", 400
    
    # defined_actions = {
    #     'get-detail' : wms_location_type.get_location_type_list,
    #     'add-location-type' : lambda : 'add-location-type function placeholder'
    # }
    # defined_actions = {
    #     'get-detail' : lambda location_type_name : wms_location_type.get_location_type_detail(location_type_name),
    #     'add-location-type' : lambda : 'add-location-type function placeholder'
    # }
    defined_actions = ['get-detail', 'add-location-type']

    if 'action' not in post_data or post_data['action'] not in defined_actions:
        return json.dumps({
            'result': 'Bad request'
        }), 400
    
    action = post_data['action'] if 'action' in post_data else None

    if action == 'get-detail':
        location_type_name = post_data['location_type'] if 'location_type' in post_data else None
        location_type_detail = wms_location_type.get_location_type_detail(location_type_name)
        return json.dumps({
            'result' : location_type_detail
        }), 200

    if action == 'add-location-type':
        location_type_name = post_data['location_type'] if 'location_type' in post_data else None
        (rows_affected, exception) = wms_location_type.add_location_type(location_type_name)
        # (rows_affected, exception)
        if exception is None:
            return json.dumps({
                'result' : "OK"
            }), 200

    return json.dumps({
        'result': 'Bad request'
    }), 400

    # defined_actions['get-detail'](location_type)
    # defined_actions['add-location-type'](location_type)

    # result = defined_actions[post_data['action']]()
    # response_data = {
    #     'result' : defined_actions[post_data['action']]()
    # }
    # return json.dumps({
    #     'result' : defined_actions[post_data['action']]()
    # }), 200


    # breadcrumbs = [
    #     { 'href' : '/wms/dashboard', 'text': 'WMS' },
    #     { 'href' : None, 'text': 'Location Type' }
    # ]
    # from forum_app.features.wms_location_type import WmsLocationTypeFeature
    # wms_location_type = WmsLocationTypeFeature()
    # location_list = wms_location_type.get_location_list()
    # return render_template(f'wms/wms_location.html', 
    #     breadcrumb_list=breadcrumbs,
    #     location_list=location_list
    #     ), 200


# @app.route('/api/wms/location/detail/<id>', methods=['GET', 'POST'])
# def api_wms_location_detail(id):
#     breadcrumbs = [
#         { 'href' : '/wms/dashboard', 'text': 'WMS' },
#         { 'href' : None, 'text': 'Location' },
#         { 'href' : None, 'text': 'Detail' }
#     ]
#     from forum_app.features.wms_location import WmsLocationFeature
#     wms_location = WmsLocationFeature()
#     if request.method == 'POST':
#         location_type_id = request.form['location_type_field']
#         location_name = request.form['location_name_field']
#         parent_location_id = None
#         wms_location.add(location_type_id, location_name, parent_location_id)
    
#     location_type_list = wms_location.get_location_type_list()
#     return render_template(f'wms/wms_location_detail.html', 
#         breadcrumb_list=breadcrumbs,
#         location_type_list=location_type_list
#         ), 200


# @app.route('/api/wms/location/add', methods=['GET', 'POST'])
# def api_wms_location_add():
#     breadcrumbs = [
#         { 'href' : '/wms/dashboard', 'text': 'WMS' },
#         { 'href' : None, 'text': 'Location' },
#         { 'href' : None, 'text': 'Add New' }
#     ]
    
#     wms_location = WmsLocationFeature()
#     if request.method == 'POST':
#         location_type_id = request.form['location_type_field']
#         location_name = request.form['location_name_field']
#         parent_location_id = None
#         wms_location.add(location_type_id, location_name, parent_location_id)
    
#     location_type_list = wms_location.get_location_type_list()
#     return render_template(f'wms/wms_location_add.html', 
#         breadcrumb_list=breadcrumbs,
#         location_type_list=location_type_list
#         ), 200
