import logging as log
from flask import render_template, redirect, url_for
from forum_app import app

@app.route('/demo/')
def test_get():
    """Web page at /demo/"""
    return redirect(url_for('demo_layout_test_page'))

@app.route('/demo/layout-test')
def demo_layout_test_page():
    """Web page at /demo/layout-test"""
    return render_template('demo/demo_layout_test_page.html')
