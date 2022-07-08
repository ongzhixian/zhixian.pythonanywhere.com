from flask import render_template, session, request, redirect, url_for
from forum_app import app

@app.route('/shared-data/')
def root_shared_data_get():
    """Web page at '/shared-data'"""
    return redirect('/shared-data/dashboard')

@app.route('/shared-data/dashboard')
def shared_data_dashboard_page():
    """Web page at '/shared-data/dashboard'"""
    return render_template('shared_data/shared_data_dashboard.html', users=[])
    