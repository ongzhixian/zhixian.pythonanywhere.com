from functools import wraps
from flask import g, request, redirect, url_for

def require_authenticated_user(f):
    @wraps(f)
    def username_check_function(*args, **kwargs):
        if 'username' not in g or g.username is None:
            return redirect(url_for('login', next=request.url))
        return f(*args, **kwargs)
    return username_check_function