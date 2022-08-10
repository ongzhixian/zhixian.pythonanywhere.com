from flask import render_template, redirect, url_for
from forum_app import app

from forum_app.features.ipf import IpfFeature

@app.route('/ipf/')
def ipf_get():
    """Re-route /ipf/ to dashboard"""
    return redirect(url_for('ipf_dashboard_page'))

@app.route('/ipf/dashboard')
def ipf_dashboard_page():
    """/ipf/dashboard"""
    ipf = IpfFeature()
    dashboard_list = ipf.get_dashboard_list()
    return render_template(
        'ipf/ipf_dashboard.html',
        dashboard_list=dashboard_list)
