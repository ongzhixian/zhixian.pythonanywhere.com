import logging
from flask import render_template, session, request, redirect, url_for
from forum_app import app, app_path
from os import path

@app.route('/shared-data/')
def root_shared_data_get():
    """Web page at '/shared-data'"""
    return redirect('/shared-data/dashboard')

@app.route('/shared-data/dashboard')
def shared_data_dashboard_page():
    """Web page at '/shared-data/dashboard'"""
    to_implement_data_list = [
        "Country codes", 
        "Market Identifier Code (MIC) (ISO 10383)",
        
        "Classification of Financial Instruments (CFI) (ISO 10962)",
        
        "International Securities Identification Number (ISIN) (ISO 6166)",
        "Committee on Uniform Securities Identification Procedures (CUSIP) number"
        "Stock Exchange Daily Official List (SEDOL)",
        "Bloomberg ticker",
        "Reuters Instrument code ticker",
        "Yahoo ticker",

        "Wertpapierkennnummer",
        "IATA ICAO",

        "Society for Worldwide Interbank Financial Telecommunication (SWIFT)",
        "Business Identifier Codes (BIC) (ISO 9362)"
        "International Bank Account Number (IBAN)",
        "Legal Entity Identifier (LEI) (ISO 17442)",
        "Data Universal Numbering System (DUNS)",
    ]
    return render_template('shared_data/shared_data_dashboard.html', users=[], to_implement_data_list=to_implement_data_list)
    
@app.route('/shared-data/country')
def shared_data_country():
    """Web page at '/shared-data/country'"""
    from forum_app.databases.forum_database import MySqlDataProvider
    db = MySqlDataProvider('forum')
    sql = """SELECT short_name, code2, code3, m49 FROM country ORDER BY short_name;"""
    record_list = db.fetch_list(sql)
    return render_template('shared_data/shared_data_country.html', country_list=record_list)


# from html.parser import HTMLParser

# class MyHTMLParser(HTMLParser):
#     def handle_starttag(self, tag, attrs):
#         print("Encountered a start tag:", tag)
#         breakpoint()

#     def handle_endtag(self, tag):
#         print("Encountered an end tag :", tag)

#     def handle_data(self, data):
#         print("Encountered some data  :", data)


def download_m49():
    # Scrape data from target_url (https://docs.python.org/3.7/library/urllib.request.html)
    out_file_path = path.join(app_path, 'data', 'shared_data', 'm49.html')
    logging.info(f'out_file_path: {out_file_path}')

    # from urllib import request
    # target_url = 'https://unstats.un.org/unsd/methodology/m49/'
    # with request.urlopen(target_url) as response:
    #     html = response.read().decode('utf-8')
    #     with open(out_file_path, 'w', encoding='utf8') as outfile:
    #         outfile.write(html)

    with open(out_file_path, 'r', encoding='utf8') as infile:
        html = infile.read()
        
    parser = MyHTMLParser()
    parser.feed(html)


def get_country_data_from_csv():
    country_codes_csv_file_path = path.join(app_path, 'data', 'comma_separated_values', 'iso-3166-country-codes-obp.csv')
    country_data = []
    
    import csv
    with open(country_codes_csv_file_path, "r", encoding="utf8") as infile:
        csv_reader = csv.reader(infile)
        next(csv_reader, None)  # skip the headers
        for row in csv_reader:
            country_data.append((row[0], row[2], row[3], row[4]))
    return country_data
    
def insert_country_data(country_data):
    from forum_app.databases.forum_database import MySqlDataProvider
    db = MySqlDataProvider('forum')
    sql = """INSERT INTO country (short_name, code2, code3, m49) VALUES (%s, %s, %s, %s)"""
    db.execute_many(sql, country_data)

def load_country_codes():
    country_data = get_country_data_from_csv()
    print(len(country_data))
    insert_country_data(country_data)


@app.route('/shared-data/country', methods=['POST'])
def shared_data_country_post():
    """Web page at '/shared-data/country'"""
    logging.info("POST to shared_data_country_post")

    action_map = {
        'download M49': download_m49,
        'load country codes': load_country_codes
    }

    if 'action' not in request.form:
        return
    
    action = request.form['action']
    action_map[action]()

    # response.status, response.reason is equivalent to (200, 'OK')
    return render_template('shared_data/shared_data_country.html')

