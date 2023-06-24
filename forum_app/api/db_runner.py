import os
import mysql.connector

from flask import render_template, session, request, redirect, url_for
from forum_app import app
from forum_app.features.logging import log
from forum_app import app_secrets, resolve_file_path

db_settings = app_secrets["MYSQL"]['forum']


def get_script_file_name(script_name):
    _, file_extension = os.path.splitext(script_name)
    if file_extension == "":
        script_file_name = f"{script_name}.sql"
    else:
        script_file_name = script_name
    return script_file_name


def run_script(script_path):
    with open(script_path, 'r') as file:
        sql = file.read()
    
    print(sql)
    try:
        connection = mysql.connector.connect(user=db_settings['USERNAME'], password=db_settings['PASSWORD'], host=db_settings['HOST'], database=db_settings['DATABASE'])
        
        cursor = connection.cursor()
        
        cursor.execute(sql)

        connection.commit()

        return "OK", 200

    except mysql.connector.Error as err:
        print(err)
        return "Internal Server Error", 500
    except Exception as ex:
        print(ex)
        return "Internal Server Error", 500
    finally:
        cursor is not None and cursor.close()
        connection is not None and connection.close()
    

@app.route('/api/db_runner/<script_name>', methods=['GET'])
def api_get_db_runner(script_name):

    try:
        script_file_name = get_script_file_name(script_name)

        script_path = resolve_file_path('forum', script_file_name)
        
        if os.path.exists(script_path):
            (status_text, status_code) = run_script(script_path)
            return status_text, status_code
        else:
            return "Not Found", 404
    except Exception as ex:
        log.error(ex)
        return "Bad Request", 400
