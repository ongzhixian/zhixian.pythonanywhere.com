import logging
from flask import render_template, session, request, redirect, url_for
from forum_app import app, app_path
from os import abort, path

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

        "GICS industry code",
        "MSCI sector code",
        "FTSE 100 sector code",

        "Wertpapierkennnummer",
        "IATA Airline",
        "IATA Airport",

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


@app.route('/shared-data/country-test')
def shared_data_country_test():
    """Web page at '/shared-data/country-test'
    Not in actual usage; used only for testing processes
    """
    record_start = 0
    page_size = 2
    data_page = 1

    if 'page' in request.args:
        try:
            data_page = int(request.args['page'])
        except ValueError:
            data_page = 1

    if data_page == 3:
        abort(500)
        
    record_start = (data_page - 1) * page_size

    from forum_app.databases.forum_database import MySqlDataProvider
    db = MySqlDataProvider('forum')
    sql = f"""
SELECT 	* 
FROM 	(
			SELECT 	CAST(@row_no := @row_no+1 AS UNSIGNED) AS row_number, short_name, code2, code3, m49 
			FROM 	country, (SELECT @row_no := 0) t
  			ORDER BY short_name 
  		) a
LIMIT {record_start}, {page_size};"""
    print(sql)
    record_list = db.fetch_list(sql)
    return render_template('shared_data/shared_data_country_test.html', country_list=record_list, prev_page=data_page-1, next_page=data_page+1)


from html.parser import HTMLParser

class AirlineParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Encountered a start tag:", tag)
        breakpoint()

    def handle_endtag(self, tag):
        print("Encountered an end tag :", tag)

    def handle_data(self, data):
        print("Encountered some data  :", data)


@app.route('/shared-data/airline')
def shared_data_airline():
    """Web page at '/shared-data/airline'"""
    url = "https://www.iata.org/en/publications/directories/code-search/?airline.page=1&airline.search="
    # from forum_app.databases.forum_database import MySqlDataProvider
    # db = MySqlDataProvider('forum')
    # sql = """SELECT short_name, code2, code3, m49 FROM country ORDER BY short_name;"""
    # record_list = db.fetch_list(sql)
    from forum_app.modules.scrape import get_airline
    get_airline(1)
    return render_template('shared_data/shared_data_airline.html')



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
        
    # parser = MyHTMLParser()
    # parser.feed(html)


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


@app.route('/shared-data/sgx/isin')
def shared_data_sgx_isin():
    """Web page at '/shared-data/country'"""
    from forum_app.databases.forum_database import MySqlDataProvider
    db = MySqlDataProvider('forum')
    # sql = """SELECT short_name, code2, code3, m49 FROM country ORDER BY short_name;"""
    # record_list = db.fetch_list(sql)
    #return render_template('shared_data/shared_data_sgx_isin.html', country_list=record_list)
    return render_template('shared_data/shared_data_sgx_isin.html', isin_list=None)


def get_isin_data_from_file():
    isin_data_file_path = path.join(app_path, 'data', 'fixed_width_formatted_text', 'sgx-isin.txt')
    isin_data = []

    import re
    regex = r"(?P<name>.{50})(?P<status>.{10})(?P<isin>.{20})(?P<code>.{10})(?P<counter>.+)"
    with open(isin_data_file_path, 'r', encoding='utf8') as infile:
        infile.readline() # skip first header line
        for line in infile:
            match_result = re.match(regex, line)
            if match_result is None:
                continue
            name = match_result.group('name').strip()
            status = match_result.group('status').strip()
            isin = match_result.group('isin').strip()
            code = match_result.group('code').strip()
            counter = match_result.group('counter').strip()
            isin_data.append([name, isin, code, counter, status])
    return isin_data


def insert_sgx_isin_data(isin_data):
    from forum_app.databases.forum_database import MySqlDataProvider
    db = MySqlDataProvider('forum')
    sql = """INSERT INTO isin (name, isin, code, counter_name, status) VALUES (%s, %s, %s, %s, %s)"""
    db.execute_many(sql, isin_data)


def load_isin_data():
    isin_data = get_isin_data_from_file()
    print(len(isin_data))
    insert_sgx_isin_data(isin_data)

@app.route('/shared-data/sgx/isin', methods=['POST'])
def shared_data_sgx_isin_post():
    """Web page at '/shared-data/country'"""
    logging.info("POST to shared_data_sgx_isin_post")

    action_map = {
        'load ISIN data': load_isin_data
    }

    if 'action' not in request.form:
        return
    
    action = request.form['action']
    action_map[action]()

    # response.status, response.reason is equivalent to (200, 'OK')
    # return render_template('shared_data/shared_data_sgx_isin.html', isin_list=None)
    return redirect(url_for('shared_data_sgx_isin'))


@app.route('/shared-data/init')
def shared_data_init():
    """Web page at '/shared-data/init'"""
    from forum_app.databases.forum_database import MySqlDataProvider
    db = MySqlDataProvider('forum')

    return render_template('shared_data/shared_data_init.html', isin_list=None)


def create_tables():
    # Run all the scripts in 
    database_scripts_path = path.join(app_path, 'data', 'feature_database_scripts', 'shared_data', 'tables')
    logging.info(f"run_create_table_scripts in {database_scripts_path}")
    from forum_app.databases.forum_database import MySqlDataProvider
    db = MySqlDataProvider('forum')
    db.run_scripts_in_path(database_scripts_path)
    


@app.route('/shared-data/init', methods=['POST'])
def shared_data_init_post():
    """Web page at '/shared-data/init'"""
    logging.info("POST to shared_data_init_post")

    action_map = {
        'Create tables': create_tables
    }

    if 'action' not in request.form:
        return
    
    action = request.form['action']
    action_map[action]()

    return redirect(url_for('shared_data_sgx_isin'))


@app.route('/shared-data/fake')
def shared_data_fake():
    """Web page at '/shared-data/fake'"""
    # from forum_app.databases.forum_database import MySqlDataProvider
    # db = MySqlDataProvider('forum')
    return render_template('shared_data/shared_data_fake.html', isin_list=None)


def generate_fake_data():
    from faker import Faker
    Faker.seed(4321)
    fake = Faker()
    
    # name = fake.name()
    logging.info(f"name: {fake.name()}")
    logging.info(f"name: {fake.name()}")
    logging.info(f"name: {fake.name()}")
    logging.info(f"name: {fake.name()}")
    pass

@app.route('/shared-data/fake', methods=['POST'])
def shared_data_fake_post():
    """Web page at '/shared-data/init'"""
    logging.info("POST to shared_data_init_post")

    action_map = {
        'Generate fake data': generate_fake_data
    }

    if 'action' not in request.form:
        return
    
    action = request.form['action']
    action_map[action]()

    return redirect(url_for('shared_data_fake'))

