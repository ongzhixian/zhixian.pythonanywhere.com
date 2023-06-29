from flask import g, render_template, request, session, redirect, url_for
from markupsafe import escape
from forum_app import app
from forum_app.features.logging import log
from markdown import markdown

from forum_app.features.security import require_authenticated_user

# from forum_app.helpers.auth import login_required
# from forum_app.modules.barcode import QRCode
# from forum_app.features.authentication import authentication_check

@app.route('/gn')
@require_authenticated_user
def gn_home():
    """Path: / (Application root)"""
    # logging.debug(f"Username: {g.username}")
    return render_template('gn/home.html')
    # return render_template('home.html')


@app.route('/gn/simulator')
@require_authenticated_user
def gn_simulator():
    """Path: / (Application root)"""
    # logging.debug(f"Username: {g.username}")
    return render_template('gn/simulator.html')
    # return render_template('home.html')
