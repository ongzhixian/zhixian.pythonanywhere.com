import importlib
import inspect
import logging

from forum_app.databases.mysql_data_provider import MySqlDataProvider
from forum_app.features import BaseFeatureInterface

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
        """
        Count total number of features.
        Previously used in registered feature page
        KIV
        """
        record = self.db.fetch_record("SELECT COUNT(*) AS 'count' FROM _feature;", None)
        if record is None:
            return -1
        return record[0]

    def get_registered_feature_list(self, filter=''):
        sql = """
SELECT  DISTINCT COALESCE(p.id, c.id) AS 'id'
        , COALESCE(p.display_name, c.display_name) AS 'display_name'
        , COALESCE(p.description, c.description) AS 'description'
        , COALESCE(p.name, c.name) AS 'name'
        , COALESCE(p.is_enable, c.is_enable) AS 'is_enable'
FROM    _feature c
LEFT OUTER JOIN
        _feature p
        ON c.ancestor_id = p.id
WHERE   c. display_name LIKE %s
ORDER BY display_name;
        """
        records = self.db.fetch_list(sql, (f"%{filter}%",))
        logging.debug(f"Registered feature list: {len(records)}")
        if records is None:
            return []
    
        return records

    def get_feature_record(self, feature_name=''):
        sql = """
SELECT id, name, display_name, description FROM _feature WHERE name = %s
        """
        return self.db.fetch_record(sql, (feature_name,) )

    def get_child_feature_list(self, feature_name=''):
        sql = """
SELECT  id, name, display_name, description
FROM    _feature 
WHERE   ancestor_id = (SELECT id FROM _feature WHERE name= %s)
ORDER BY level
        """
        return self.db.fetch_list(sql, (feature_name,) )

