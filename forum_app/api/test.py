# 
################################################################################
# Modules and functions import statements
################################################################################

import json
import logging

from os import environ
from datetime import datetime
from time import time

from flask import request, make_response, abort

from forum_app import app, secrets
from forum_app.databases.forum_database import ForumDatabase



@app.route('/api/test/mysql', methods=['GET', 'POST'])
def api_test_mysql():

    logging.info("In api_test_mysql()")

    mydb = ForumDatabase()
    mydb.init_new_tables()
    # mydb.getDatabase()
    # mydb.create_table('create_weblink')

    
    # sec1 = os.getenv('BASH_SECRET')
    # sec2 = os.getenv('OTHER_SECRET')

    # app_secrets_file = open('/home/zhixian/.app-secrets.json')
    # app_secrets = json.load(app_secrets_file)
    # return str(app_secrets)
    return "asd"

    # return str(os.environ)
    #return str(sec1) + ' -- ' + str(sec2)



    