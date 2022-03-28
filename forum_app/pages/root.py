import logging
from flask import render_template, request, session, redirect
from forum_app import app
from forum_app.helpers.auth import login_required
from forum_app.modules.forum_db import ForumDb

@app.route('/')
@login_required
def root_get():
    """GET /"""
    return render_template('root_get.html')

@app.route('/forum')
@login_required
def forum_get():
    """GET /"""
    return render_template('forum_get.html')

@app.route('/link-dump', methods=['GET', 'POST'])
@login_required
def link_dump_get():
    """GET /"""
    if request.method == 'POST':
        url_text = request.form['urlText']
        url_list = url_text.splitlines()
        data = []
        if len(url_list) > 0:
            for url in url_list:
                data.append((url, ))
            mydb = ForumDb()
            mydb.add_weblinks(data)
    
    return render_template('link_dump_get.html')