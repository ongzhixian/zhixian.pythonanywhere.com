from flask import render_template, redirect, url_for
from forum_app import app

from forum_app.features.wms import WmsFeature

@app.route('/wms/')
def wms_get():
    """Web page at '/wms'"""
    return render_template('wms/wms_dashboard.html')
    # return redirect(url_for('wms_dashboard_page'))

@app.route('/wms/dashboard')
def wms_dashboard_page():
    """Web page at /wms/dashboard"""
    wms = WmsFeature()
    dashboard_list = wms.get_dashboard_list()
    return render_template(
        'wms/wms_dashboard.html',
        dashboard_list=dashboard_list)
