import json
from flask import render_template, session, request, redirect, url_for
from forum_app import app
from forum_app.features.logging import log
import mysql.connector
from forum_app import app_secrets
import sys

db_settings = app_secrets["MYSQL"]['forum']

# import hashlib
# m = hashlib.sha256()
# m.update(b"Nobody inspects")
# m.update(b" the spammish repetition")
# m.digest()

# hashlib.sha256(f"{salt}{password}".encode('utf-8')).hexdigest()

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

        # cursor.execute("INSERT INTO employees (first_name) VALUES (%s), (%s)", ('Jane', 'Mary'))
        # query = "INSERT INTO gn_user ()"
        # add_salary = ("INSERT INTO salaries "
        #       "(emp_no, salary, from_date, to_date) "
        #       "VALUES (%(emp_no)s, %(salary)s, %(from_date)s, %(to_date)s)")
        # data_salary = {
        # 'emp_no': emp_no,
        # 'salary': 50000,
        # 'from_date': tomorrow,
        # 'to_date': date(9999, 1, 1),
        # }
        # cursor.execute(add_salary, data_salary)


        sql = ("insert into gn_user (name, first_name, last_name, password_hash, password_salt, cre_dt, cre_id, upd_dt, upd_id) "
               "VALUES (%(username)s, '', '', %(password_salt)s, %(password_hash)s, %(cre_dt)s, %(cre_id)s, %(upd_dt)s, %(upd_id)s);")
        
        from datetime import datetime
        sql_values = {
            'username': username,
            'password_salt': 'somesalt',
            'password_hash': 'somehash',
            'cre_dt': datetime.utcnow(),
            'cre_id': 0,
            'upd_dt': datetime.utcnow(),
            'upd_id': 0,

        }

        cursor.execute(sql, sql_values)
        connection.commit()

        # #for (first_name, last_name, hire_date) in cursor:
        # for (id, name) in cursor:
        #     # print("{}, {} was hired on {:%d %b %Y}".format(
        #     #     last_name, first_name, hire_date))
        #     # result = {
        #     #     last_name: last_name, 
        #     #     first_name: first_name, 
        #     #     hire_date: hire_date
        #     # }
        #     result = {
        #         id: id, 
        #         name: name, 
        #         'version': sys.version
        #     }


    except Exception as ex:
        print(ex)
    finally:
        cursor is not None and cursor.close()
        connection is not None and connection.close()
                

@app.route('/api/gn/gn-user', methods=['POST'])
def api_post_gn_user():
    if not request.is_json:
        return "Bad Request", 400

    json_data = request.json
    add_gn_user(json_data['username'], json_data['password'])
    print(json_data)
    return "OK", 200



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

