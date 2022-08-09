from flask import render_template, redirect, url_for
from forum_app import app

from forum_app.features.wms import WmsFeature
from forum_app.features.wms_location import WmsLocationFeature
from forum_app.features.wms_location_type import WmsLocationTypeFeature

@app.route('/wms/location-type/')
def wms_location_type_get():
    """Web page at '/wms'"""
    # return render_template('wms/wms_location_type_list.html')
    return redirect(url_for('wms_location_type_list'))

@app.route('/wms/location-type/list')
def wms_location_type_list():
    """Web page at /wms/location-type/list"""
    breadcrumbs = [
        { 'href' : '/wms/dashboard', 'text': 'WMS' },
        { 'href' : None, 'text': 'Location Type List' }
    ]
    wms = WmsFeature()
    wms_location = WmsLocationFeature()
    wms_location_type = WmsLocationTypeFeature()
    location_list = wms_location.get_location_list()
    wms_location_type_list = wms_location_type.get_location_type_list()
    
    dashboard_list = wms.get_dashboard_list()
    return render_template(
        'wms/wms_location_type_list.html',
        breadcrumbs=breadcrumbs,
        dashboard_list=dashboard_list,
        wms_location_type_list = wms_location_type_list,
        location_list=location_list)
