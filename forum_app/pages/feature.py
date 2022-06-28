from flask import render_template, session, request, redirect, url_for
from forum_app import app

@app.route('/feature/')
def root_feature_get():
    """Web page at '/feature'"""
    return redirect('/feature/dashboard')

@app.route('/feature/dashboard')
def feature_dashboard_page():
    """Web page at '/feature/dashboard'"""
    return render_template('feature/feature_dashboard.html')
    