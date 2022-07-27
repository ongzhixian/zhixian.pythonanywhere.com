from flask import render_template, redirect, url_for
from forum_app import app


@app.route('/wms/')
def wms_get():
    """Web page at '/investment'"""
    return redirect(url_for('wms_dashboard_page'))

@app.route('/wms/dashboard')
def wms_dashboard_page():
    """Web page at '/wms/dashboard'"""
    return render_template('wms/wms_dashboard.html')
