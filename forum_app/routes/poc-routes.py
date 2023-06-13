from flask import g, render_template, request, session, redirect, url_for
from markupsafe import escape
from forum_app import app, app_secrets
from forum_app.features.logging import log
from forum_app.features.mongodb import MongoDb

@app.route('/poc')
def poc():
    db = MongoDb(app_secrets['mongodb:minitools:ConnectionString'], 'minitools')
    a = db.get_database()
    return render_template('poc.html', model=a)

