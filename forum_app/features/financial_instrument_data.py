import json
import logging
from os import path
from functools import wraps
from unicodedata import name
from flask import redirect, url_for, g, request
from forum_app import app_path
from forum_app.features import BaseFeatureInterface, is_feature_enable
from forum_app.pages import menu
from forum_app.modules import app_state, log

import csv
import xml.dom.minidom
import pdb
import re

from forum_app.databases.forum_database import MySqlDataProvider
        

class FinancialInstrumentDataFeature(BaseFeatureInterface):

    def __init__(self):
        super().__init__()
        self.db = MySqlDataProvider('forum')

    @property
    def feature_name(self):
        """feature_name getter property. (required)"""
        return "Financial Instrument Data"

    @property
    def feature_description(self):
        """feature_description getter property. (required)"""
        return "Enables financial instrument data module"

    def initialize(self):
        """Things to do when feature is initialized (eg. restore state from persistence storage) (on initialize_features)"""
        super().initialize()
        self.register()

    def get_sgx_isin_data_from_file(self):
        isin_data_file_path = path.join(app_path, 'data', 'fixed_width_formatted_text', 'sgx-isin.txt')
        isin_data = []

        regex = r"(?P<name>.{50})(?P<status>.{10})(?P<isin>.{20})(?P<ticker>.{10})(?P<ticker_name>.+)"
        with open(isin_data_file_path, 'r', encoding='utf8') as infile:
            infile.readline() # skip first header line
            for line in infile:
                match_result = re.match(regex, line)
                if match_result is None:
                    continue
                name = match_result.group('name').strip()
                status = match_result.group('status').strip()
                isin = match_result.group('isin').strip()
                ticker = match_result.group('ticker').strip()
                ticker_name = match_result.group('ticker_name').strip()
                isin_data.append([name, isin, 'XSES', ticker, ticker_name, status])
        return isin_data

    def insert_sgx_isin_data(self, isin_data):
        sql = """INSERT INTO instrument (name, isin, mic, ticker, ticker_name, remarks) VALUES (%s, %s, %s, %s, %s, %s)"""
        self.db.execute_many(sql, isin_data)

    def load_sgx_isin_data_to_instrument_table(self):
        record_count = self.db.fetch_value('SELECT COUNT(*) AS `record_count` FROM instrument WHERE mic = %s;', ('XSES',))
        if record_count > 0:
            return
        isin_data_list = self.get_sgx_isin_data_from_file()
        self.insert_sgx_isin_data(isin_data_list)


    def get_six_equity_data_from_csv(self):
        equity_data_file_path = path.join(app_path, 'data', 'comma_separated_values', 'six_equity_issuers.csv')
        # Note: six_equity_issuers.csv is actually delimited by semi-colon (;) and not comma (,)
        instrument_data = []

        #  0 - Company                              |ABB Ltd
        #  1 - Symbol                               |ABBN
        #  2 - Valor Number                         |1222171
        #  3 - Country                              |CH
        #  4 - Traded Currency                      |CHF
        #  5 - Trading platform                     |XSWX
        #  6 - Class of Share                       |Registered Share
        #  7 - Nominal Value                        |0.12
        #  8 - Listing Segment                      |International Reporting Standard
        #  9 - Accounting Rules                     |US GAAP
        # 10 - Next General Meeting                 |23.03.2023
        # 11 - Annual closing date                  |31.12.
        # 12 - Auditors                             |KPMG AG - CH[501403]
        # 13 - Sustainability report opting in      |No
        # 14 - International recognized standard    |
        # 15 - Primary listing                      |TRUE
        # 16 - Opting Clause                        |

        with open(equity_data_file_path, "r") as infile:
            csv_reader = csv.reader(infile, delimiter=';', )
            next(csv_reader, None)  # skip the headers
            for row in csv_reader:
                name = row[0]
                valor = row[2]
                mic = row[5]
                ticker = row[1]
                currency = row[4]
                instrument_data.append([name, valor, mic, ticker, currency])
        return instrument_data

    def insert_six_equity_data(self, isin_data):
        sql = """INSERT INTO instrument (name, valor, mic, ticker, currency) VALUES (%s, %s, %s, %s, %s)"""
        self.db.execute_many(sql, isin_data)

    def load_six_data_to_instrument_table(self):
        record_count = self.db.fetch_value('SELECT COUNT(*) AS `record_count` FROM instrument WHERE mic = %s;', ('XSWX',))
        if record_count > 0:
            return
        six_equity_data = self.get_six_equity_data_from_csv()
        self.insert_six_equity_data(six_equity_data)

    def get_oanda_asset_class_from_tags(self, tags):
        if len(tags) <= 0:
            return None
        asset_class_map = {
            'CFD': 1,
            'METAL': 1,
            'CURRENCY': 1
        }

    def get_oanda_instrument_data_from_json(self):
        oanda_instrument_data_file_path = path.join(app_path, 'data', 'json', 'oda-instruments.json')
        instrument_data = []
        
        with open(oanda_instrument_data_file_path, "r") as infile:
            oanda_instrument_json = json.load(infile)
        if 'instruments' not in oanda_instrument_json:
            return instrument_data
        oanda_instruments = oanda_instrument_json['instruments']
        for instrument in oanda_instruments:
            name = instrument['displayName']
            ticker = instrument['name']
            instrument_type = instrument['type']
            tags = {}
            if 'tags' in instrument:
                tag_list = instrument['tags']
                for tag in tag_list:
                    tag_type = tag['type']
                    tag_name = tag['name']
                    tags[tag_type] = tag_name
            asset_class = self.get_oanda_asset_class_from_tags(tags)

            logging.debug(f"{name}, {ticker}, {instrument_type}, {len(tags)}")

            # instrument_data.append([name, valor, mic, ticker, currency])
            # csv_reader = csv.reader(infile, delimiter=';', )
            # next(csv_reader, None)  # skip the headers
            # for row in csv_reader:
            #     name = row[0]
            #     valor = row[2]
            #     mic = row[5]
            #     ticker = row[1]
            #     currency = row[4]
            #     instrument_data.append([name, valor, mic, ticker, currency])
        # return instrument_data
        # TODO:

    def load_oanda_data_to_instrument_table(self):
        oanda_data = self.get_oanda_instrument_data_from_json()

    def register(self):
        if self.is_registered(self.feature_name):
            return
        
        database_table_scripts_path = path.join(app_path, 'data', 'feature_database_scripts', 'financial_instrument_data', 'tables')
        self.db.run_scripts_in_path(database_table_scripts_path)
        # On load, we load the following data
        # 1. Instrument types (skipped for now; implicitly loaded by the instrument type table script)
        # 2. Instruments
        self.load_sgx_isin_data_to_instrument_table()
        self.load_six_data_to_instrument_table()
        # TODO: load data for the following exchanges
        # XJPX -- Japan         : WWW.JPX.CO.JP
        # XFRA -- Germany       : WWW.DEUTSCHE-BOERSE.COM
        # XHKG -- Hong Kong     : WWW.HKEX.COM.HK   https://www.hkex.com.hk/Mutual-Market/Stock-Connect/Eligible-Stocks/View-All-Eligible-Securities?sc_lang=en
        # XLUX -- Luxembourg    : WWW.BOURSE.LU
        # XNAS -- US            : WWW.NASDAQ.COM
        # UK
        # MY
        self.load_oanda_data_to_instrument_table()
        # https://www.citibank.com/mss/about/assets/docs//Stock_Connect_Handbook_Feb2017.pdf
        # self.populate_country_table()
        # self.populate_currency_table()
        # self.populate_market_identifier_table()
        # self.register_classification_of_financial_instruments()
        # 
        # self.register_feature(self.feature_name, self.feature_description, __name__)

    def app_state_changed(self, event_data=None):
        """Things to do whenever app_state changed"""
        if not self.is_my_event(event_data):
            return
        # We want to selective add/remove logins menu item to admin menu in drawer
        # authentication_login_menu_item_id = "authentication-logins"
        # log.debug(f"{self.feature_name} is_enable: {self.is_enable} event_data {event_data}")
        # if self.is_enable:
        #     logging.debug("Add to drawer_admin_menu")
        #     app_state.add_to_menu('drawer_admin_menu', 
        #         authentication_login_menu_item_id, "Logins", "/user/dashboard", False, "table_rows",)
        # else:
        #     # Remove login menu item to admin menu in drawer
        #     logging.debug("Remove drawer_admin_menu")
        #     app_state.remove_from_menu('drawer_admin_menu', 
        #         authentication_login_menu_item_id)
            
