import json
from flask import render_template, session, request, redirect, url_for
from forum_app import app
from forum_app.features.logging import log
import mysql.connector



@app.route('/api/wms/customer', methods=['GET'])
def api_get_wms_customer():
    result = "asd"
    # cnx = mysql.connector.connect(user='scott', password='password', host='127.0.0.1', database='employees')
    # cnx.close()

    if result is None:
        return "Bad request", 400
    else:
        return str(result)
