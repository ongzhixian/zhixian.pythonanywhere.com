import logging

from functools import wraps
from flask import g, request, redirect, url_for
from flask import session, redirect, request, abort


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not 'username' in g:
            logging.info("Username not in g")
            return redirect(url_for('login', next=request.url))
        return f(*args, **kwargs)
    return decorated_function


# def authorize(f):
#     @wraps(f)
#     def decorated_function(*args, **kws):
#             if not 'Authorization' in request.headers:
#                abort(401)

#             user = None
#             data = request.headers['Authorization'].encode('ascii','ignore')
#             token = str.replace(str(data), 'Bearer ','')
#             try:
#                 user = jwt.decode(token, JWT_SECRET, algorithms=['HS256'])['sub']
#             except:
#                 abort(401)

#             return f(user, *args, **kws)            
#     return decorated_function


