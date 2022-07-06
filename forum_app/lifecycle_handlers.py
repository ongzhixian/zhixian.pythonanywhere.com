import logging
from flask import g, current_app, request, session, redirect, url_for, abort
from forum_app import app

@app.before_request
def before_each_request():
    if "username" in session:
        g.username = session["username"]
    # admin menu syntax: <display-text>, <href>, <icon>
    g.admin_menu = [
        ("Inb", "/inb/dashboard", "table_rows")
    ]
    g.app_menu = [
        ("Oub", "/oub/dashboard", "table_rows")
    ]
    

@app.context_processor
def inject_feature_menu_items():
    # get feature menu items
    menu_items = [
        ("Inv xxxxxx", "/inv/dashboard", "table_rows"),
        ("Inv yyyyyy", "/inv/dashboard", "table_rows"),
    ]
    return dict(feature_menu_items=menu_items)


@app.context_processor
def inject_login_menu_items():
    # get login menu items
    # Menu item tuple format:
    # (display-text, href, disabled)
    # ("Profile ()", "/dummy", False)
    menu_items = [
        ("Profile", "/dummy", False),
        ("Change password", "/dummy", False),
        ("Settings", "/dummy", True),
        ("Log out", "/dummy", False)
    ]
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
