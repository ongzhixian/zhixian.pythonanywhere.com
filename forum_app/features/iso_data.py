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

from forum_app.databases.forum_database import MySqlDataProvider
        

class ISODataFeature(BaseFeatureInterface):

    def __init__(self):
        super().__init__()
        self.db = MySqlDataProvider('forum')

    @property
    def feature_name(self):
        """feature_name getter property. (required)"""
        return "ISO Data"

    @property
    def feature_description(self):
        """feature_description getter property. (required)"""
        return "Enables ISO data module"

    def initialize(self):
        """Things to do when feature is initialized (eg. restore state from persistence storage) (on initialize_features)"""
        super().initialize()
        self.register()


    def load_country_codes_from_csv(self):
        country_codes_csv_file_path = path.join(app_path, 'data', 'comma_separated_values', 'iso-3166-country-codes-obp.csv')
        country_data = []
        with open(country_codes_csv_file_path, "r", encoding="utf8") as infile:
            csv_reader = csv.reader(infile)
            next(csv_reader, None)  # skip the headers
            for row in csv_reader:
                country_data.append((row[0], row[2], row[3], row[4]))
        return country_data
    
    def insert_country_data(self, country_data):
        sql = """INSERT INTO country (short_name, code2, code3, m49) VALUES (%s, %s, %s, %s)"""
        self.db.execute_many(sql, country_data)

    def populate_country_table(self):
        record_count = self.db.fetch_value('SELECT COUNT(*) AS `record_count` FROM country;')
        if record_count > 0:
            return
        country_code_list = self.load_country_codes_from_csv()
        self.insert_country_data(country_code_list)


    def get_child_element_value(self, element, child_element_tag_name):
        child_elements = element.getElementsByTagName(child_element_tag_name)
        return None if len(child_elements) <= 0 else child_elements[0].firstChild.nodeValue.strip()

    def get_currency_codes_from_xml(self):
        # Read XML data 
        xml_file_path = path.join(app_path, 'data', 'xml', 'currency-codes-iso-4217.xml')

        # Note: xml.dom.minidom is not secure against maliciously constructed data; used only with trusted data sources.
        docs = xml.dom.minidom.parse(xml_file_path)
        code_list = []
        ccy_list = docs.getElementsByTagName("CcyNtry")
        for ccy in ccy_list:
            country_name = self.get_child_element_value(ccy, "CtryNm")
            currency_name = self.get_child_element_value(ccy, "CcyNm")
            # is_fund = self..get_child_element_attribute_value(ccy, "CcyNm", "IsFund")
            currency_code = self.get_child_element_value(ccy, "Ccy")
            currency_number = self.get_child_element_value(ccy, "CcyNbr")
            currency_minor_unit = self.get_child_element_value(ccy, "CcyMnrUnts")
            currency_minor_unit = int(currency_minor_unit) if currency_minor_unit is not None and currency_minor_unit.isdigit() else None
            code_list.append([country_name, currency_name, currency_code, currency_number, currency_minor_unit])
        return code_list

    def insert_currency_data(self, currency_code_list):
        sql = """INSERT INTO currency (country_name, name, code, number, minor_unit) VALUES (%s, %s, %s, %s, %s)"""
        self.db.execute_many(sql, currency_code_list)

    def populate_currency_table(self):
        record_count = self.db.fetch_value('SELECT COUNT(*) AS `record_count` FROM currency;')
        if record_count > 0:
            return
        currency_code_list = self.get_currency_codes_from_xml()
        self.insert_currency_data(currency_code_list)
    

    def get_market_identifier_codes_from_csv(self):
        mic_csv_file_path = path.join(app_path, 'data', 'comma_separated_values', 'iso-10383-market-identifier-codes.csv')
        mic_data = []
        with open(mic_csv_file_path, "r", encoding="utf8") as infile:
            csv_reader = csv.reader(infile)
            next(csv_reader, None)  # skip the headers
            for row in csv_reader:
                mic_data.append((row[0], row[1], row[2], row[3], row[5], row[6], row[7], row[8], row[10], row[12]))
            # 00 - "COUNTRY",
            # 01 - "ISO COUNTRY CODE (ISO 3166)",
            # 02 - "MIC",
            # 03 - "OPERATING MIC",
            # 04 - "O/S",
            # 05 - "NAME-INSTITUTION DESCRIPTION",
            # 06 - "ACRONYM",
            # 07 - "CITY",
            # 08 - "WEBSITE",
            # 09 - "STATUS DATE",
            # 10 - "STATUS",
            # 11 - "CREATION DATE",
            # 12 - "COMMENTS"
        return mic_data

    def insert_market_identifier_data(self, market_identifier_code_list):
        sql = """INSERT INTO market_identifier (country_name, country_code2, code, operating_mic, name, short_name, city, url, status, comments)  VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
        self.db.execute_many(sql, market_identifier_code_list)


    def populate_market_identifier_table(self):
        record_count = self.db.fetch_value('SELECT COUNT(*) AS `record_count` FROM market_identifier;')
        if record_count > 0:
            return
        market_identifier_code_list = self.get_market_identifier_codes_from_csv()
        logging.debug(len(market_identifier_code_list))
        self.insert_market_identifier_data(market_identifier_code_list)

    def register(self):
        if self.is_registered(self.feature_name):
            return
        
        database_table_scripts_path = path.join(app_path, 'data', 'feature_database_scripts', 'iso_data', 'tables')
        self.db.run_scripts_in_path(database_table_scripts_path)
        # On load, we load the following ISO data
        # 1. ISO-3166   Country Codes
        # 2. ISO-4217   Currency Codes
        # 2. ISO-10383  Market Identifier Codes (MIC)
        # 4. ISO-10962  Classification of Financial Instruments (CFI)
        self.populate_country_table()
        self.populate_currency_table()
        self.populate_market_identifier_table()
        # self.register_classification_of_financial_instruments()
        self.register_feature(self.feature_name, self.feature_description, __name__)

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
            
