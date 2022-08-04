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
