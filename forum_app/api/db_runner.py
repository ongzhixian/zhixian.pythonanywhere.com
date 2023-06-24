import json
from flask import render_template, session, request, redirect, url_for
from forum_app import app
from forum_app.features.logging import log
import mysql.connector
from forum_app import app_secrets
import sys

db_settings = app_secrets["MYSQL"]['forum']
print(db_settings)

@app.route('/api/db_runner/<script_name>', methods=['GET'])
def api_get_db_runner(script_name):

    # C:\src\github.com\ongzhixian\pythonanywhere.com\forum_app\data\database-scripts\mysql\forum\gn-tables.sql
    import os

    file_name, file_extension = os.path.splitext(script_name)
    if file_extension == "":
        print("no file extension; append!")
        print(file_extension)
        script_file_name = f"{script_name}.sql"
    else:
        script_file_name = script_name

    script_path = os.path.join(os.getcwd(), 'run/forum', script_file_name)

    
    print(script_path)
    ex = os.path.exists(script_path)
    print(ex)

    return f"{script_name} {ex} {script_path}"
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

