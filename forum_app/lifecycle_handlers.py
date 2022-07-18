import logging
from flask import g, current_app, request, session, redirect, url_for, abort
from forum_app import app
# from forum_app.pages import menu
from forum_app.modules import app_state

@app.before_request
def before_each_request():
    # if "username" in session:
    #     logging.debug("username is in session")
    #     g.username = session["username"]
    g.username = session["username"] if "username" in session else None
    g.roles = session["roles"] if "roles" in session else None
    g.application = session["application"] if "application" in session else None

# Defining menu items for various menus
# Note: It is possible to define menu on g as well like so:
# g.admin_menu = [
#     ("Inb", "/inb/dashboard", "table_rows")
# ]

def get_menu_items(menu_name):
    """Get menu items from app_state (if exists); else return []"""
    return app_state.menu[menu_name].menu_items.values() if menu_name in app_state.menu else []

@app.context_processor
def inject_drawer_sitemap_menu():
    menu_items = get_menu_items('drawer_sitemap_menu')
    return dict(drawer_sitemap_menu=menu_items)

@app.context_processor
def inject_drawer_admin_menu():
    menu_items = get_menu_items('drawer_admin_menu')
    return dict(drawer_admin_menu=menu_items)

@app.context_processor
def inject_header_menu():
    menu_items = get_menu_items('header_menu')
    return dict(header_menu=menu_items)

@app.context_processor
def inject_selected_application():
    """App state value for selected application"""
    app_state_value = app_state.value['selected_application'] if 'selected_application' in app_state.value else None
    return dict(selected_application=app_state_value)

@app.context_processor
def inject_application_menu_items():
    menu_items = get_menu_items('application_menu')
    return dict(application_menu_items=menu_items)


@app.context_processor
def inject_login_menu_items():
    # get login menu items
    # Menu item tuple format:
    # (display-text, href, disabled)
    # ("Profile ()", "/dummy", False)
    menu_items = get_menu_items('login_menu')
    # menu_items = [
    #     ("Profile", "/dummy", False),
    #     ("Change password", "/dummy", False),
    #     ("Settings", "/dummy", True),
    #     ("Log out", "/dummy", False)
    # ]
    return dict(login_menu_items=menu_items)

# @app.errorhandler(Exception)
# def all_exception_handler(error):
#     return 'Error:' + str(error), 500

# @app.errorhandler(400)
# def bad_request(e):
#     return 'Bad request', 400

# @app.errorhandler(401)
# def unauthorized(e):
#     return 'Unauthorized', 401

# @app.errorhandler(403)
# def forbidden(e):
#     return 'Forbidden', 403

# @app.errorhandler(404)
# def not_found(e):
#     return 'Not found', 404

# @app.errorhandler(500)
# def internal_server_error(e):
#     return 'Internal server error', 500
#     # note that we set the 404 status explicitly
#     # return render_template('404.html'), 404

# @app.errorhandler(502)
# def bad_gateway(e):
#     return 'Bad gateway', 502

# @app.errorhandler(503)
# def service_unavailable(e):
#     return 'Service unavailable', 503

# @app.errorhandler(504)
# def gateway_timeout(e):
#     return 'Gateway timeout', 504
