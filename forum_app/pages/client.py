import logging
from flask import render_template, session, request, redirect, url_for
from forum_app import app, app_path
from os import abort, path

@app.route('/client/')
def root_client_get():
    """Web page at '/client'"""
    return redirect('/client/dashboard')

@app.route('/client/dashboard')
def client_dashboard_page():
    """Web page at '/client/dashboard'"""
    return render_template('client/client_dashboard.html')


@app.route('/client/new')
def client_new_page():
    """Web page at '/client/new'"""
    return render_template('client/new_client.html')

@app.route('/client/new', methods=['POST'])
def client_new_post():
    """Web page at '/client/new'"""
    client_name_field = request.form.get("client_name_field")
    

    from forum_app.features.client import ClientFeature
    client = ClientFeature()
    rows_affected = client.add_new(client_name_field)

    return render_template('client/new_client.html')


    # Insert mic data


# def get_mic_from_csv_file():
#     mic_csv_file_path = path.join(app_path, 'data', 'comma_separated_values', 'iso-10383-market-identifier-codes.csv')
#     mic_data = []

#     # 00 - "COUNTRY",
#     # 01 - "ISO COUNTRY CODE (ISO 3166)",
#     # 02 - "MIC",
#     # 03 - "OPERATING MIC",
#     # 04 - "O/S",
#     # 05 - "NAME-INSTITUTION DESCRIPTION",
#     # 06 - "ACRONYM",
#     # 07 - "CITY",
#     # 08 - "WEBSITE",
#     # 09 - "STATUS DATE",
#     # 10 - "STATUS",
#     # 11 - "CREATION DATE",
#     # 12 - "COMMENTS"

#     import csv
#     with open(mic_csv_file_path, "r", encoding="utf8") as infile:
#         csv_reader = csv.reader(infile)
#         next(csv_reader, None)  # skip the headers
#         for row in csv_reader:
#             mic_data.append((row[0], row[1], row[2], row[3], row[5], row[6], row[7], row[8], row[10], row[12]))
#     return mic_data

# def insert_mic_data():
#     mic_list = get_mic_from_csv_file()
#     from forum_app.databases.forum_database import MySqlDataProvider
#     db = MySqlDataProvider('forum')
#     sql = """INSERT INTO market_identifier (country_name, country_code2, code, operating_mic, name, short_name, city, url, status, comments)  VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
#     db.execute_many(sql, mic_list)


# @app.route('/shared-data/mic', methods=['POST'])
# def shared_data_mic_post():
#     """Web page at '/shared-data/currency'"""
#     logging.info("POST to shared_data_currency_post")

#     action_map = {
#         'Insert mic data': insert_mic_data
#     }

#     if 'action' not in request.form:
#         return
    
#     action = request.form['action']
#     action_map[action]()

#     return redirect(url_for('shared_data_mic'))