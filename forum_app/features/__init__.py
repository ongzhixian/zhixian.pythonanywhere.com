################################################################################
# Define package composition
################################################################################

__all__ = ["authentication", "login"]

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

    def register_feature(self, feature_name, feature_description) -> bool:
        """Register feature into system"""
        rows_affected = self.db.execute(
            "INSERT INTO _feature (name, description) VALUES (%s, %s);", 
            (feature_name, feature_description))
        print(f"Rows affected {rows_affected}")
        return rows_affected > 0

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
    