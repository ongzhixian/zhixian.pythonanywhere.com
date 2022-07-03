################################################################################
# Define package composition
################################################################################

__all__ = ["authentication", "login"]

from forum_app.modules.mysqldb import MySqlDatabase

class BaseFeatureInterface:
    """Defines interface for feature"""

    def __init__(self):
        self.db = MySqlDatabase('forum')
    
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

    def register(self):
        """Register feature into system"""
        pass
    