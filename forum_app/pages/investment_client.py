import logging
from flask import render_template, session, request, redirect, url_for
from forum_app import app, app_path
from os import abort, path

@app.route('/investment/client/')
def root_client_get():
    """Web page at '/client'"""
    return redirect('/investment/client/dashboard')

@app.route('/investment/client/dashboard')
def client_dashboard_page():
    """Web page at '/client/dashboard'"""
    from forum_app.features.investment_client import ClientFeature
    client = ClientFeature()
    records = client.get_client_list()
    client_type_list = client.get_client_type_list()
    selected_client_type = 1
    return render_template('client/client_dashboard.html', 
        client_type_list=client_type_list,
        client_list=records,
        selected_client_type=selected_client_type)

@app.route('/investment/client/dashboard', methods=['POST'])
def client_dashboard_post():
    """Web page at '/client/dashboard'"""
    client_name = request.form.get("client_name_field")
    client_type_dropdown = request.form.get("client_type_dropdown")
    logging.debug(f"client_name {client_name},  client_type_dropdown {client_type_dropdown}")
    from forum_app.features.investment_client import ClientFeature
    client = ClientFeature()
    records = client.get_client_list(client_name, client_type_dropdown)
    client_type_list = client.get_client_type_list()
    return render_template('client/client_dashboard.html', 
        client_type_list=client_type_list,
        client_list=records, 
        search_term=client_name,
        selected_client_type=client_type_dropdown,)


@app.route('/client/new')
def client_new_page():
    """Web page at '/client/new'"""
    # Get a list of client types
    # SELECT id, name FROM client_type ORDER BY name;
    from forum_app.features.investment_client import ClientFeature
    client = ClientFeature()
    client_type_list = client.get_client_type_list()
    selected_client_type = 1
    return render_template('client/new_client.html', 
        selected_client_type=selected_client_type,
        client_type_list=client_type_list)

@app.route('/client/new', methods=['POST'])
def client_new_post():
    """Web page at '/client/new'"""
    client_name_field = request.form.get("client_name_field")
    client_type_dropdown = request.form.get("client_type_dropdown")

    from forum_app.features.investment_client import ClientFeature
    client = ClientFeature()
    rows_affected = client.add_new(client_name_field, client_type_dropdown)
    client_type_list = client.get_client_type_list()
    message = 'Success' if rows_affected > 0 else 'Failed'
    return render_template('client/new_client.html', 
        selected_client_type=client_type_dropdown,
        client_type_list=client_type_list,
        message=message)


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