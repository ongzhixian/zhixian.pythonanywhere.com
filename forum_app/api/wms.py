import json
from flask import render_template, session, request, redirect, url_for
from forum_app import app
from forum_app.features.logging import log
import mysql.connector
from forum_app import app_secrets
import sys

db_settings = app_secrets["MYSQL"]['forum']

@app.route('/api/wms/customer', methods=['GET'])
def api_get_wms_customer():
    result = "asd"

    try:
        connection = mysql.connector.connect(user=db_settings['USERNAME'], password=db_settings['PASSWORD'], host=db_settings['HOST'], database=db_settings['DATABASE'])
        cursor = connection.cursor()

        # with mysql.connector.connect(user=db_settings['USERNAME'], password=db_settings['PASSWORD'], host=db_settings['HOST'], database=db_settings['DATABASE']) as connection, connection.cursor() as cursor:
            # query = ("SELECT first_name, last_name, hire_date FROM employees ")
            # query = "SELECT first_name, last_name, hire_date FROM employees "
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




def sample_api_get_wms_customer():
    result = "asd"
    # Note: Python 3.9 supports using 'with' for connection and cursor
    # however this does not work on PythonAnywhere (unsure why)
    connection = mysql.connector.connect(user=db_settings['USERNAME'], password=db_settings['PASSWORD'], host=db_settings['HOST'], database=db_settings['DATABASE'])
    cursor = connection.cursor()

    # query = ("SELECT first_name, last_name, hire_date FROM employees "
    #         "WHERE hire_date BETWEEN %s AND %s")

    # hire_start = datetime.date(1999, 1, 1)
    # hire_end = datetime.date(1999, 12, 31)

    # cursor.execute(query, (hire_start, hire_end))

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


    query = ("SELECT first_name, last_name, hire_date FROM employees ")
    cursor.execute(query)

    for (first_name, last_name, hire_date) in cursor:
        print("{}, {} was hired on {:%d %b %Y}".format(
            last_name, first_name, hire_date))

    cursor.close()
    connection.close()

    if result is None:
        return "Bad request", 400
    else:
        return str(result)
