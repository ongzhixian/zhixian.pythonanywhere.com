# 
################################################################################
# Modules and functions import statements
################################################################################

import json
import logging

from os import environ, path
from datetime import datetime
from time import time,sleep

from flask import request, make_response, abort

from forum_app import app, app_path
from forum_app.databases.forum_database import ForumDatabase

@app.route('/api/test/upload-file', methods=['GET', 'POST'])
def api_test_upload_file():
    logging.debug("api_test_upload_file called")
    for file_key in request.files:
        upload_file = request.files[file_key]
        if upload_file.filename.endswith('-close-plot.png'):
            upload_file.save(path.join(app_path, 'wwwroot', 'images', 'external-charts', upload_file.filename))
        else:
            upload_file.save(path.join(app_path, "data", "uploads", upload_file.filename))
    
    return "OK", 200
    

@app.route('/api/test/download-file', methods=['GET', 'POST'])
def api_test_download_file():
    pass



# @api.route("/files/<filename>", methods=["POST"])
# def post_file(filename):
#     """Upload a file."""

#     if "/" in filename:
#         # Return 400 BAD REQUEST
#         abort(400, "no subdirectories allowed")

#     with open(os.path.join(UPLOAD_DIRECTORY, filename), "wb") as fp:
#         fp.write(request.data)

#     # Return 201 CREATED
#     return "", 201


# @app.route('/api/test/oda', methods=['GET', 'POST'])
# def api_test_oda():
#     logging.info("In api_test_mysql()")
#     json_file_path = path.join(app_path, 'data', 'json', 'oda-instruments.json')
#     with open(json_file_path, 'r', encoding='utf-8') as json_file:
#         data = json.load(json_file) # Load the JSON data

#     sleep(1.678) # sleep for 1.678 seconds    
#     return json.dumps(data)


# @app.route('/api/test/exec', methods=['GET', 'POST'])
# def api_test_exec():
#     logging.info("In api_test_mysql()")
#     json_file_path = path.join(app_path, 'data', 'json', 'oda-instruments.json')
#     with open(json_file_path, 'r', encoding='utf-8') as json_file:
#         data = json.load(json_file) # Load the JSON data
#     return json.dumps(data)



# @app.route('/api/test/mysql', methods=['GET', 'POST'])
# def api_test_mysql():

#     logging.info("In api_test_mysql()")

#     mydb = ForumDatabase()
#     mydb.init_new_tables()
#     # mydb.getDatabase()
#     # mydb.create_table('create_weblink')

    
#     # sec1 = os.getenv('BASH_SECRET')
#     # sec2 = os.getenv('OTHER_SECRET')

#     # app_secrets_file = open('/home/zhixian/.app-secrets.json')
#     # app_secrets = json.load(app_secrets_file)
#     # return str(app_secrets)
#     return "asd"

#     # return str(os.environ)
#     #return str(sec1) + ' -- ' + str(sec2)



    