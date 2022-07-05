################################################################################
# Define package composition
################################################################################

__all__ = ["forum_database", "mysql_data_provider"]

class BaseDataProviderInterface:
    """Defines interface for data provider"""

    def get_connection(self):
        """Returns a connection object (if applicable)"""
        pass

    def create_database_if_not_exists(self) -> bool:
        """Create database if not exists"""
        return

    # There are 2 fetch (fetchone, fetchall)
    # To change to:
    # 1. fetch_value        -- return a single value
    # 2. fetch_record       -- return a single record (tuple)
    # 3. fetch_list         -- return a list of records (tuples)
    # 4. fetch_record_sets  -- return result_sets
    
    def fetch_value(self, sql, args=None):
        """Return a single value"""
        pass

    def fetch_record(self, sql, args=None):
        """Return a single record"""
        pass

    def fetch_list(self, sql, args=None):
        """Return a single list"""
        pass

    def fetch_record_sets(self, sql, args=None):
        """Return a single record_sets"""
        pass


class BaseDatabaseInterface:
    """Defines interface for database"""

    def create_database_if_not_exists(self):
        """Create database if not exists"""
        return

    def is_missing_key_tables(self):
        """Checks if database is missing key tables"""
        return