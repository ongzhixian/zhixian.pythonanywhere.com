import logging
import pdb

from forum_app.databases import BaseDatabaseInterface
from forum_app.databases.mysql_data_provider import MySqlDataProvider


class ForumDatabase(BaseDatabaseInterface):
    def __init__(self):
        self.db = MySqlDataProvider('forum')

    def create_database_if_not_exists(self):
        """Create database if not exists"""
        self.db.create_database_if_not_exists()
        return

    def is_missing_key_tables(self):
        """Checks if database is missing key tables"""
        # Application should have minimally 3 tables
        # 1.    _db_migrate
        # 2.    _feature
        # 3.    _menu?
        required_table_list = ('_db_migrate', '_feature', '_menu')
        format_strings = ','.join(['%s'] * len(required_table_list))
        sql = "SELECT TABLE_NAME FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_SCHEMA = 'forum' AND TABLE_NAME IN ({0});".format(format_strings)
        records = self.db.fetch_list(sql, required_table_list)
        if len(records) == len(required_table_list):
            return
        # Carry out recovery action here
        self.db.initialize_database()

    # _db_migrate

    def add_db_migrate(self, file_path):
        (rows_affected, _) = self.db.execute(
            "INSERT INTO _db_migrate (file_path) VALUES (%s);", (file_path,))
        logging.info(f"add_db_migrate (rows affected): [{rows_affected}]")
        
    def db_migrate_exists(self, file_path):
        record = self.db.fetch_record(
            "SELECT 1 FROM _db_migrate WHERE file_path = %s;", (file_path,))
        record_exists = record is not None
        logging.info(f"db_migrate_exists: [{record_exists}]")
        return record_exists

    def get_unapplied_db_migrate_count(self):
        record = self.db.fetch_record(
            "SELECT COUNT(id) AS 'COUNT' FROM _db_migrate WHERE apply_dt IS NULL;", None)
        return record[0]

    def get_unapplied_db_migrate_list(self):
        records = self.db.fetch_list(
            "SELECT id, file_path, cre_dt FROM _db_migrate WHERE apply_dt IS NULL;", None)
        return records

    def get_schema_object_count(self):
        record = self.db.fetch_record(
            "SELECT table_count, view_count, procedure_count, function_count FROM schema_object_count;", None)
        return record