import logging
from flask import g, request, session, redirect, url_for
from forum_app import app

@app.before_request
def before_each_request():
    if "username" in session:
        g.username = session["username"]
    