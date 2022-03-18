import logging
from flask import render_template, session, redirect
from forum_app import app
from forum_app.helpers.auth import login_required

@app.route('/')
@login_required
def root_get():
    """GET /"""
    if 'username' not in session:
        return redirect('/login')
    return render_template('root_get.html')