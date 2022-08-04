from flask import render_template, redirect, url_for
from forum_app import app

from forum_app.features.wms import WmsFeature
from forum_app.features.wms_location import WmsLocationFeature

@app.route('/wms/location/')
def wms_location_get():
    """Web page at '/wms'"""
    return render_template('wms/wms_location_list.html')
    # return redirect(url_for('wms_location_list'))

@app.route('/wms/location/list')
def wms_location_list():
    """Web page at /wms/location/list"""
    breadcrumbs = [
        { 'href' : '/wms/dashboard', 'text': 'WMS' },
        { 'href' : None, 'text': 'Location List' }
    ]
    wms = WmsFeature()
    wms_location = WmsLocationFeature()
    location_list = wms_location.get_location_list()

    dashboard_list = wms.get_dashboard_list()
    return render_template(
        'wms/wms_location_list.html',
        breadcrumbs=breadcrumbs,
        dashboard_list=dashboard_list,
        location_list=location_list)

@app.route('/wms/location/add')
def wms_location_add():
    """Web page at /wms/location/add"""
    breadcrumbs = [
        { 'href' : '/wms/dashboard', 'text': 'WMS' },
        { 'href' : None, 'text': 'Location Add' }
    ]
    wms = WmsFeature()
    wms_location = WmsLocationFeature()
    location_list = wms_location.get_location_list()

    wms_location = WmsLocationFeature()
    # if request.method == 'POST':
    #     location_type_id = request.form['location_type_field']
    #     location_name = request.form['location_name_field']
    #     parent_location_id = None
    #     wms_location.add(location_type_id, location_name, parent_location_id)
    
    location_type_list = wms_location.get_location_type_list()

    dashboard_list = wms.get_dashboard_list()
    return render_template(
        'wms/wms_location_add.html',
        breadcrumbs=breadcrumbs,
        dashboard_list=dashboard_list,
        location_type_list=location_type_list,
        location_list=location_list)
