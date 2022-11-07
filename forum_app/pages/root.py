import logging
from flask import g, render_template, request, session, redirect
from forum_app import app
# from forum_app.helpers.auth import login_required
# from forum_app.modules.barcode import QRCode
# from forum_app.features.authentication import authentication_check

@app.route('/')
# @authentication_check
def root_get():
    """Path: / (Application root)"""
    # logging.debug(f"Username: {g.username}")
    return render_template('root.jinja')



# @app.route('/favicon.ico')
# # @authentication_check
# def favicon_ico_get():
#     """Path: /favicon.ico"""
#     # logging.debug(f"Username: {g.username}")
#     # return render_template('root_get.html')
#     return "", 201
