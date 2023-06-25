import json
from flask import render_template, session, request, redirect, url_for
from forum_app import app
from forum_app.features.logging import log
import mysql.connector
from forum_app import app_secrets
import sys

db_settings = app_secrets["MYSQL"]['forum']

@app.route('/api/gn/gn-user', methods=['GET'])
def api_get_gn_user():
    
    try:
        connection = mysql.connector.connect(user=db_settings['USERNAME'], password=db_settings['PASSWORD'], host=db_settings['HOST'], database=db_settings['DATABASE'])
        cursor = connection.cursor()
        sql = "SELECT id, name FROM gn_user;"
        cursor.execute(sql)
        results = []

        for (id, name) in cursor:
            results.append({
                id: id, 
                name: name
            })
            
        return json.dumps(results), 200, {'Content-Type': 'application/json; charset=utf-8'}

    except Exception as ex:
        print(ex)
    finally:
        cursor is not None and cursor.close()
        connection is not None and connection.close()

def add_gn_user(username, password):
    try:
        connection = mysql.connector.connect(user=db_settings['USERNAME'], password=db_settings['PASSWORD'], host=db_settings['HOST'], database=db_settings['DATABASE'])
        cursor = connection.cursor()

        sql = ("insert into gn_user (name, first_name, last_name, password_salt, password_hash, cre_dt, cre_id, upd_dt, upd_id) "
               "VALUES (%(username)s, '', '', %(password_salt)s, %(password_hash)s, %(cre_dt)s, %(cre_id)s, %(upd_dt)s, %(upd_id)s);")
        
        from datetime import datetime
        from secrets import token_urlsafe
        import hashlib
        salt = token_urlsafe(4)
        hash_hex = hashlib.sha256(f"{salt}{password}".encode('utf-8')).hexdigest()
        
        sql_values = {
            'username': username,
            'password_salt': salt,
            'password_hash': hash_hex,
            'cre_dt': datetime.utcnow(),
            'cre_id': 0,
            'upd_dt': datetime.utcnow(),
            'upd_id': 0,

        }
        print(sql, sql_values)
        cursor.execute(sql, sql_values)
        connection.commit()
        return "Created", 201
    except Exception as ex:
        print("exception happened")
        print(ex)
        # Executed with errors (250); Check server logs
        return "Executed with errors", 250
    finally:
        cursor is not None and cursor.close()
        connection is not None and connection.close()

@app.route('/api/gn/gn-user', methods=['POST'])
def api_post_gn_user():
    if not request.is_json:
        return "Bad Request", 400

    json_data = request.json
    (status_text, status_code) = add_gn_user(json_data['username'], json_data['password'])
    print(json_data)
    return status_text, status_code


@app.route('/api/gn/customer', methods=['GET'])
def api_get_gn_customer():

    try:
        connection = mysql.connector.connect(user=db_settings['USERNAME'], password=db_settings['PASSWORD'], host=db_settings['HOST'], database=db_settings['DATABASE'])
        cursor = connection.cursor()

        query = "SELECT id, name FROM wms_customer "
        cursor.execute(query)

        #for (first_name, last_name, hire_date) in cursor:
        for (id, name) in cursor:
            # print("{}, {} was hired on {:%d %b %Y}".format(
            #     last_name, first_name, hire_date))
            # result = {
            #     last_name: last_name, 
            #     first_name: first_name, 
            #     hire_date: hire_date
            # }
            result = {
                id: id, 
                name: name, 
                'version': sys.version
            }


    except Exception as ex:
        print(ex)
    finally:
        cursor is not None and cursor.close()
        connection is not None and connection.close()

    if result is None:
        return "Bad request", 400
    else:
        return str(result)

