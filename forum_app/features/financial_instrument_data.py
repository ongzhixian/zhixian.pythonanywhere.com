import logging
from os import path
from functools import wraps
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

    def get_isin_data_from_file(self):
        isin_data_file_path = path.join(app_path, 'data', 'fixed_width_formatted_text', 'sgx-isin.txt')
        isin_data = []

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
                isin_data.append([name, isin, 'XSES', code, counter, status, 0])
        return isin_data

    def insert_sgx_isin_data(self, isin_data):
        sql = """INSERT INTO instrument (name, isin, mic, ticker, ticker_name, remarks, type_id) VALUES (%s, %s, %s, %s, %s, %s, %s)"""
        self.db.execute_many(sql, isin_data)

    def load_sgx_isin_data_to_instrument_table(self):
        isin_data_list = self.get_isin_data_from_file()
        self.insert_sgx_isin_data(isin_data_list)


    def register(self):
        if self.is_registered(self.feature_name):
            return
        
        database_table_scripts_path = path.join(app_path, 'data', 'feature_database_scripts', 'financial_instrument_data', 'tables')
        self.db.run_scripts_in_path(database_table_scripts_path)
        # On load, we load the following data
        # 1. Instrument types (skipped for now; implicitly loaded by the instrument type table script)
        # 2. Instruments
        self.load_sgx_isin_data_to_instrument_table()
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
            
