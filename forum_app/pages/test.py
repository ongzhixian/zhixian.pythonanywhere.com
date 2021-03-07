import logging as log
from flask import render_template, request
from forum_app import app

@app.route('/test/')
def test_get():
    """Web page at '/'"""
    #return app.config
    return render_template('test_get.html')

@app.route('/test/add')
def test_add_get():
    """Web page at '/'"""
    #return app.config
    return render_template('test_add_get.html')

@app.route('/test/add', methods=['POST'])
def test_add_post():
    """Web page at '/'"""

    topic_title     = request.form['topic_title']
    topic_content   = request.form['topic_content']

    log.info(f"topic_title is {topic_title}")
    log.info(f"topic_content is {topic_content}")

    return render_template('test_add_get.html')