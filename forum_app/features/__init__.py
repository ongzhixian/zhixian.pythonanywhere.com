################################################################################
# Define package composition
################################################################################

__all__ = ["authentication", "login"]

import logging
from forum_app import app_settings
from forum_app.modules.mysqldb import MySqlDatabase

class BaseFeatureInterface:
    """Defines interface for feature"""

    def __init__(self):
        self.db = MySqlDatabase('forum')
        self.is_enable = False
    
    def is_registered(self, feature_name) -> bool:
        """Register feature into system"""
        record = self.db.fetch_one(
            "SELECT 1 FROM _feature WHERE name = %s;", 
            (feature_name,))
        if record is None:
            return False
        return True

    def register_feature(self, feature_name, feature_description, module_name) -> bool:
        """Register feature into system"""
        rows_affected = self.db.execute(
            "INSERT INTO _feature (name, description, module_name) VALUES (%s, %s, %s);", 
            (feature_name, feature_description, module_name))
        return rows_affected > 0

    def toggle_enable(self, feature_name, enable):
        """Update is_enable flag for feature"""
        rows_affected = self.db.execute("""
UPDATE  _feature 
SET		is_enable = %s
WHERE	name = %s;
""", (enable, feature_name))
        logging.debug(f"Rows affected {rows_affected}")

        changes_saved = rows_affected > 0

        if changes_saved:
            # Update global app_settings
            (is_enable, module_name) = self.get_enable_setting_by_name(feature_name)
            if module_name not in app_settings:
                app_settings[module_name] = {}
            app_settings[module_name]["is_enable"] = is_enable

        return changes_saved

    def get_enable_setting(self, module_name):
        record = self.db.fetch_one(
            "SELECT is_enable FROM _feature WHERE module_name = %s;", 
            (module_name,))
        if record is None:
            return False
        return record[0] == 1

    def get_enable_setting_by_name(self, name):
        record = self.db.fetch_one(
            "SELECT is_enable, module_name FROM _feature WHERE name = %s;", 
            (name,))
        if record is None:
            return (None, None)
        return (record[0], record[1])

    def load(self):
        """Things to do whenever feature is loaded"""
        pass

    def register(self):
        """Register feature into system"""
        pass

    def load_app_settings(self, app_settings):
        """Load app_settings (from storage) """
        pass

    def update_app_settings(self, app_settings):
        """Define/Set app_settings """
        pass
    