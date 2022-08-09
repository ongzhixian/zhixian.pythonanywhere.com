# 
################################################################################
# Modules and functions import statements
################################################################################

import logging
import json
from flask import render_template, request

from forum_app import app, app_path
from forum_app.features.wms_location import WmsLocationFeature

@app.route('/api/wms/location-type', methods=['GET', 'POST'])
def api_wms_location_type():
    posts_data = request.json
    # {'location_type': 'Building'}
    response_data = {
        'location_type' : posts_data['location_type'],
        'data' : 'some custom data'
    }
    return json.dumps(response_data), 200
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


