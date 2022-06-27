import logging
from flask import g, request, session, redirect, url_for, abort
from forum_app import app

@app.before_request
def before_each_request():
    if "username" in session:
        g.username = session["username"]

@app.errorhandler(Exception)
def all_exception_handler(error):
    return 'Error:' + str(error), 500

@app.errorhandler(400)
def bad_request(e):
    return 'Bad request', 400

@app.errorhandler(401)
def unauthorized(e):
    return 'Unauthorized', 401

@app.errorhandler(403)
def forbidden(e):
    return 'Forbidden', 403

@app.errorhandler(404)
def not_found(e):
    return 'Not found', 404

@app.errorhandler(500)
def internal_server_error(e):
    return 'Internal server error', 500
    # note that we set the 404 status explicitly
    # return render_template('404.html'), 404

@app.errorhandler(502)
def bad_gateway(e):
    return 'Bad gateway', 502

@app.errorhandler(503)
def service_unavailable(e):
    return 'Service unavailable', 503

@app.errorhandler(504)
def gateway_timeout(e):
    return 'Gateway timeout', 504
