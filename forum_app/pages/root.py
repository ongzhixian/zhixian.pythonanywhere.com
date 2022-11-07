import logging
from flask import g, render_template, request, session, redirect
from markupsafe import escape
from forum_app import app

# from forum_app.helpers.auth import login_required
# from forum_app.modules.barcode import QRCode
# from forum_app.features.authentication import authentication_check

from forum_app import wiki

@app.route('/')
# @authentication_check
def root_get():
    """Path: / (Application root)"""
    # logging.debug(f"Username: {g.username}")
    return render_template('root.jinja')

@app.route("/wiki/")
def wiki_default_page_get():
    return render_template('wiki.jinja', wiki_content=wiki.get_wiki_content(None), wiki_title="")

@app.route("/wiki/<string:title>")
def wiki_page_get(title):
    stored_wiki_content = f"Hello, {escape(title)}!"
    return render_template('wiki.jinja', wiki_content=stored_wiki_content)

@app.route("/wiki-editor/")
def wiki_editor_default_page_get():
    return render_template('wiki-editor.jinja', wiki_content=wiki.get_wiki_content(None), wiki_title="")


# @app.route('/favicon.ico')
# # @authentication_check
# def favicon_ico_get():
#     """Path: /favicon.ico"""
#     # logging.debug(f"Username: {g.username}")
#     # return render_template('root_get.html')
#     return "", 201
