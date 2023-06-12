import logging
from flask import g, current_app, request, session, redirect, url_for, abort
from forum_app import app

@app.before_request
def before_each_request():
    if "username" in session:
        logging.debug("username is in session")
        g.username = session["username"]
    # g.username = session["username"] if "username" in session else None
    # g.roles = session["roles"] if "roles" in session else None
    # g.application = session["application"] if "application" in session else None
    # g.is_development = app_state.is_development
    # # Get menu (depends if its accessed by authenticated user)
    # menu_items = BaseMenuInterface().get_menu_items(g.username)
    # # breakpoint()
    # g.menu_items = menu_items
    