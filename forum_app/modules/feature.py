import os

import hashlib
import base64
import logging
import pdb

import importlib
import inspect

from forum_app.features import BaseFeatureInterface

from forum_app.databases.mysql_data_provider import MySqlDataProvider

class Feature:
    def __init__(self):
        self.db = MySqlDataProvider('forum')

    def register_built_in_features(self):
        logging.info("Register built-in feature")
        from forum_app.features import __all__ as feature_list
        for feature in feature_list:
            feature_module = importlib.import_module(f"forum_app.features.{feature}")
            class_member_list = inspect.getmembers(feature_module, inspect.isclass)
            for class_member in class_member_list:
                feature_class = class_member[1]
                is_feature = issubclass(feature_class, BaseFeatureInterface)
                if is_feature:
                    feature_instance = feature_class()
                    feature_instance.register()

    def diagnose(self):
        logging.info("Diagnose")
        pass

    def get_registered_feature_count(self):
        record = self.db.fetch_record(
            "SELECT COUNT(*) AS 'count' FROM _feature;", None)
        
        if record is None:
            return -1

        return record[0]
        
        # m = hashlib.sha256()
        # stored_password_hash = login_record[1]
        # stored_password_salt = login_record[2]
        # salted_password = stored_password_salt.encode("utf8") + password.encode("utf8")
        # m.update(salted_password)

        # password_hash = m.hexdigest()
        # return password_hash == stored_password_hash

    def get_registered_feature_list(self):
        records = self.db.fetch_list(
            "SELECT * FROM _feature;", None)
        
        if records is None:
            return []
    
        return records
    

    # def add(self, username, password):
    #     print("Executing add_weblink")
    #     # Need to generate salt and hash

    #     password_salt = base64.b64encode(os.urandom(8))
    #     m = hashlib.sha256()

    #     salted_password = password_salt + password.encode("utf8")
    #     m.update(salted_password)
    #     password_hash = m.hexdigest()

    #     rows_affected = self.db.execute(
    #         "INSERT INTO login (username, password_salt, password_hash) VALUES (%s, %s, %s);", 
    #         (username, password_salt, password_hash))
    #     print(f"Rows affected {rows_affected}")
    #     return rows_affected

    # def is_valid_credential(self, username, password):
    #     login_record = self.db.fetch_one(
    #         "SELECT username, password_hash, password_salt FROM `login` WHERE username = %s;", 
    #         (username,))
    #     if login_record is None:
    #         return False
        
    #     m = hashlib.sha256()
    #     stored_password_hash = login_record[1]
    #     stored_password_salt = login_record[2]
    #     salted_password = stored_password_salt.encode("utf8") + password.encode("utf8")
    #     m.update(salted_password)

    #     password_hash = m.hexdigest()
    #     return password_hash == stored_password_hash

#     def get_users(self):
#         sql = """
# SET @row_number = 0;
# SELECT	(@row_number:=@row_number + 1) AS row_num
# 		, id
#         , username
# FROM	login
# ORDER BY username
# LIMIT 25;
#         """
#         return self.db.fetch_batch(sql)
        
