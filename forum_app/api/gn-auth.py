import hashlib
import json
import time
from datetime import datetime, timedelta, timezone
from secrets import token_urlsafe
from uuid import uuid4

import jwt
import mysql.connector
from flask import redirect, render_template, request, session, url_for

from forum_app import app, app_secrets, app_settings
from forum_app.features.logging import log

# Experimental
# import logging
# logger = logging.getLogger('')
# logger.info('This is a warning')
# log.infox('a log call in module body (not in any function)')
# log.infox("Some OPERATION", operation="myfun", status=400, status_text="Bad request", status_description="Request is not JSON", )

db_settings = app_secrets["MYSQL"]['forum']

# /api/gn/auth-ticket           [POST] pass credentials -> auth-ticket
# /api/gn/check-auth-ticket     [POST] pass jwt -> valid/invalid
# /api/gn/refresh-auth-ticket   [POST] pass jwt -> new JWT

@app.route('/api/gn/auth-ticket', methods=['POST'])
def api_post_gn_auth_ticket():
    """Generate auth ticket
    Takes a username-password pair and returns a JWT if they are valid credentials
    """
    OPERATION="Generate auth ticket"

    (is_valid_request, json_data) = validate_auth_ticket_request(request)

    if not is_valid_request:
        log.info(OPERATION, result="Bad Request (400)")
        return "Bad Request", 400

    user_record = get_validated_user_record(json_data['username'], json_data['password'])
    
    if user_record is None:
        log.info(OPERATION, result="Bad Request (400)")
        return "Invalid", 400
    
    encoded_data = get_bearer_token(user_record)
    
    log.info(OPERATION, result="OK (200)")
    return json.dumps(encoded_data), 200, {'Content-Type': 'application/json; charset=utf-8'}


@app.route('/api/gn/check-auth-ticket', methods=['POST'])
def api_post_gn_check_ticket():
    """Validate auth ticket
    Takes a JWT in request body and returns OK if JWT is valid (can be decoded)
    """
    
    OPERATION = "Validate auth ticket"

    if not request.is_json:
        return "Bad Request", 400
    
    json_data = request.json

    try:
        json_jwt = json_data['body']
        token = json_jwt
        decoded_data = jwt.decode(
            jwt=token,
            key=app_secrets['JWT_SECRET_KEY'],
            algorithms=["HS256"],
            audience=app_settings['jwt']['audience'])
        
        log.info(OPERATION, result="OK (200)")
        return "OK", 200
        
    except jwt.exceptions.InvalidSignatureError as ex:
        log.warning(OPERATION, result="Invalid token (250)")
        return "Invalid token", 250
    except Exception as ex:
        log.warning(OPERATION, result="Exception (500)", exception=str(ex))
        return "Exception", 500

    # return json.dumps(results), 200, {'Content-Type': 'application/json; charset=utf-8'}
    # return decoded_data, 200, {'Content-Type': 'application/json; charset=utf-8'}

    # (status_text, status_code) = add_gn_user(json_data['username'], json_data['password'])
    # print(json_data)
    # return status_text, status_code


@app.route('/api/gn/refresh-auth-ticket', methods=['POST'])
def api_post_gn_refresh_ticket():
    """refresh-auth
    Takes a JWT in request header and returns new ticket is JWT is valid
    """
    
    OPERATION = "Refresh auth ticket"

    if 'Bearer' not in request.headers:
        return "Bad Request", 400

    try:
        decoded_data = jwt.decode(
            jwt=request.headers['Bearer'],
            key=app_secrets['JWT_SECRET_KEY'],
            algorithms=["HS256"],
            audience=app_settings['jwt']['audience'])
        
        print(decoded_data)
        # 'iat': 1687658956, 'nbf': 1687658956, 'exp': 1687662556
        
        iat = time.localtime(decoded_data['iat'])
        nbf = time.localtime(decoded_data['nbf'])
        exp = time.localtime(decoded_data['exp'])

        # time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(1687658956))
        print(f'iat {iat}')
        print(f'nbf {nbf}')
        print(f'exp {exp}')
        check_time = time.localtime()

        if check_time < nbf:
            return "Bad request (too early; nbf check failed)", 400
        if check_time > exp:
            return "Bad request (expired; exp checked failed)", 400
        
        # OK to re-issue auth-ticket
        encoded_data = get_renew_token(decoded_data)
    
        log.info(OPERATION, result="OK (200)")
        return json.dumps(encoded_data), 200, {'Content-Type': 'application/json; charset=utf-8'}
        
    except jwt.exceptions.InvalidSignatureError as ex:
        log.warning(OPERATION, result="Invalid token (250)")
        return "Invalid token", 250
    except Exception as ex:
        log.warning(OPERATION, result="Exception (500)", exception=str(ex))
        return "Exception", 500

    # return json.dumps(results), 200, {'Content-Type': 'application/json; charset=utf-8'}
    # return decoded_data, 200, {'Content-Type': 'application/json; charset=utf-8'}

    # (status_text, status_code) = add_gn_user(json_data['username'], json_data['password'])
    # print(json_data)
    # return status_text, status_code


# 'PRIVATE' METHODS

def validate_auth_ticket_request(request):
    
    if not request.is_json:
        return False, None

    if 'username' not in request.json or 'password' not in request.json:
        return False, None

    return True, request.json

def retrieve_user_record(username):
    """Returns dictionary of 
    {
        name: name,
        password_hash: password_hash,
        password_salt: password_salt
    }
    else None
    """
    try:
        connection = mysql.connector.connect(user=db_settings['USERNAME'], password=db_settings['PASSWORD'], host=db_settings['HOST'], database=db_settings['DATABASE'])
        cursor = connection.cursor()

        sql = ("SELECT name, password_salt, password_hash FROM gn_user WHERE name = %(username)s;")
        
        sql_values = {
            'username': username,
        }

        cursor.execute(sql, sql_values)

        for (name, password_salt, password_hash) in cursor:
            return {
                'name': name,
                'password_hash': password_hash,
                'password_salt': password_salt
            }
    except Exception as ex:
        log.error(ex)
    finally:
        cursor is not None and cursor.close()
        connection is not None and connection.close()
    return None

def get_validated_user_record(username, password):
    try:
        user_record = retrieve_user_record(username)
        
        hash_hex = hashlib.sha256(f"{user_record['password_salt']}{password}".encode('utf-8')).hexdigest()

        if hash_hex == user_record['password_hash']:
            return {
                'username': user_record['name']
            }
        
    except Exception as ex:
        log.error(ex)
        # # Executed with errors (250); Check server logs
        # return "Executed with errors", 250
    return None

def get_bearer_token(user_record):
    claims_data = {
        "iat": datetime.now(tz=timezone.utc),
        "nbf": datetime.now(tz=timezone.utc),
        "exp": datetime.now(tz=timezone.utc) + timedelta(minutes=app_settings['jwt']['expiry_minutes']),
        "iss": app_settings['jwt']['issuer'],
        "aud": app_settings['jwt']['audience'],
        "jti": uuid4().hex,
        "sub": user_record['username'],
        "email": user_record['username'],
    }

    encoded_data = jwt.encode(payload=claims_data,
                              key=app_secrets['JWT_SECRET_KEY'],
                              algorithm="HS256")
                              
    return encoded_data

def get_renew_token(claims):
    claims_data = {
        "iat": datetime.now(tz=timezone.utc),
        "nbf": datetime.now(tz=timezone.utc),
        "exp": datetime.now(tz=timezone.utc) + timedelta(minutes=app_settings['jwt']['expiry_minutes']),
        "iss": app_settings['jwt']['issuer'],
        "aud": app_settings['jwt']['audience'],
        "jti": uuid4().hex,
        "sub": claims['sub'],
        "email": claims['email'],
    }

    encoded_data = jwt.encode(payload=claims_data,
                              key=app_secrets['JWT_SECRET_KEY'],
                              algorithm="HS256")
                              
    return encoded_data