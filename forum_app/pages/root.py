from flask import render_template
from forum_app import app

@app.route('/')
def root_get():
    """Web page at '/'"""
    #return app.config
    return render_template('index.html')