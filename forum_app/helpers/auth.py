import logging

from functools import wraps
from flask import g, request, redirect, url_for
from flask import session, redirect, request, abort
from forum_app import app_settings

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        dependent_feature_name = 'forum_app.features.authentication'
        
        if dependent_feature_name in app_settings and "is_enable" in app_settings[dependent_feature_name]:
            is_enabled = app_settings[dependent_feature_name]["is_enable"]
            if (is_enabled and 'username' in g) or (not is_enabled):
                # Authentication is not switched on -OR- is on and is authenticated; display whatever
                logging.info(f"OK {app_settings}")
                return f(*args, **kwargs)
        
        logging.info(f"NG {app_settings}")
        
        return redirect(url_for('login', next=request.url))
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


