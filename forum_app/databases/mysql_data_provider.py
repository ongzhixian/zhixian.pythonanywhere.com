import logging
from os import environ, path, walk
from sqlite3 import connect

from forum_app import app_secrets, app_path
from forum_app.databases import BaseDataProviderInterface

import mysql.connector

class MySqlDataProvider(BaseDataProviderInterface):
    """Data provider for MySql"""

    def __init__(self, database_setting_name):
        prefix = ''
        if 'PYTHONANYWHERE_DOMAIN' not in environ:
            prefix = 'dev_'
        setting_name = f'{prefix}{database_setting_name}'
        self.database_setting_name = database_setting_name
        self.db_settings = app_secrets['MYSQL'][setting_name]
        self.database_name = self.db_settings['DATABASE']

    def create_database_if_not_exists(self):
        """Create database if not exists"""
        database_name = self.db_settings['DATABASE']

        connection = self.get_server_connection()
        mycursor = connection.cursor()

        is_database_missing = self.is_database_missing(mycursor, database_name)
        if is_database_missing:
            self.run_create_database_script(mycursor, self.database_setting_name)

        mycursor.close()
        connection.close()

        if is_database_missing:
            self.initialize_database(self.database_setting_name)

    def initialize_database(self, database_name = None):
        if database_name is None:
            database_name = self.database_setting_name

        connection = self.get_connection()
        mycursor = connection.cursor()

        self.run_create_table_scripts(mycursor, database_name)
        self.run_create_view_scripts(mycursor, database_name)

        mycursor.close()
        connection.close()


    def run_create_table_scripts(self, cursor, database_name):
        database_scripts_path = path.join(app_path, 'data', 'database_initialization_scripts', database_name, 'tables')
        logging.info(f"run_create_table_scripts in {database_scripts_path}")
        self.run_scripts_in_path(database_scripts_path, cursor)
        
    def run_create_view_scripts(self, cursor, database_name):
        database_scripts_path = path.join(app_path, 'data', 'database_initialization_scripts', database_name, 'views')
        logging.info(f"run_create_view_scripts in {database_scripts_path}")
        self.run_scripts_in_path(database_scripts_path, cursor)
        

    def run_scripts_in_path(self, database_scripts_path, cursor = None):
        did_not_bring_cursor = cursor is None

        if did_not_bring_cursor:
            connection = self.get_connection()
            cursor = connection.cursor()

        for dirpath, _, files in walk(database_scripts_path):
            for file_name in files:
                script_file_path = path.join(dirpath, file_name)
                file_relative_path = path.relpath(script_file_path, database_scripts_path)
                script_file_is_missing = not path.exists(script_file_path)
                
                logging.info(f"Found file_relative_path [{file_relative_path}]")
                if script_file_is_missing:
                    logging.warning(f"{script_file_path} missing; script execution skipped.")
                    continue
                
                try: # Load script
                    with open(script_file_path) as db_script_file:
                        sql_script = db_script_file.read()
                    
                    result_sets = cursor.execute(sql_script, None, multi=True)
                    for result_set in result_sets:
                        pass
                    logging.info(f"Executed {file_relative_path}")
                except Exception as e:
                    logging.error(e)
                    # logging.info("Some error occurred", e)
        
        if did_not_bring_cursor:
            cursor.close()
            connection.close()


    def run_create_database_script(self, cursor, database_name):
        database_create_script = f"create-{database_name}.sql"
        database_creation_script_path = path.join(app_path, 'data', 'database_creation_scripts', database_create_script)
        script_file_is_missing = not path.exists(database_creation_script_path)
        sql_script = ''

        if script_file_is_missing:
            logging.warning(f"{database_creation_script_path} missing; database creation skipped.")
            return
        
        with open(database_creation_script_path) as db_script_file:
            sql_script = db_script_file.read()
        cursor.execute(sql_script, None, multi=True)

    # def run_scripts(self, database_scripts_path):
    #     connection = self.get_connection()
    #     mycursor = connection.cursor()
    #     self.run_scripts_in_path(mycursor, database_scripts_path)
    #     mycursor.close()
    #     connection.close()
        

    def is_database_missing(self, cursor, database_name):
        cursor.execute(
            "SELECT DISTINCT 1 FROM INFORMATION_SCHEMA.SCHEMATA WHERE SCHEMA_NAME = %s",
            (database_name,))
        record = cursor.fetchone()
        return record is None

    def get_connection(self):
        mydb = mysql.connector.connect(
            host=self.db_settings['HOST'],
            port=self.db_settings['PORT'],
            user=self.db_settings['USERNAME'],
            password=self.db_settings['PASSWORD'],
            database=self.db_settings['DATABASE'],
            collation='utf8mb4_unicode_ci',
            charset='utf8mb4'
        )
        return mydb

    def get_server_connection(self):
        mydb = mysql.connector.connect(
            host=self.db_settings['HOST'],
            port=self.db_settings['PORT'],
            user=self.db_settings['USERNAME'],
            password=self.db_settings['PASSWORD'],
            collation='utf8mb4_unicode_ci',
            charset='utf8mb4'
        )
        return mydb

    # Note:
    # With statements does not work on Python 3.7 :-(
    # with self.get_connection() as connection, connection.cursor() as mycursor:
    #     mycursor.execute(sql)
    #     return mycursor.fetchone()

    def fetch_value(self, sql, args=None):
        """Return a single value"""
        connection = self.get_connection()
        mycursor = connection.cursor()
        mycursor.execute(sql, args)
        result = mycursor.fetchone()
        mycursor.close()
        connection.close()
        return None if result is None else result[0]

    def fetch_record(self, sql, args=None):
        """Return a single record"""
        connection = None
        mycursor = None
        try:
            connection = self.get_connection()
            mycursor = connection.cursor()
            mycursor.execute(sql, args)
            result = mycursor.fetchone()
            return result
        except Exception as ex:
            logging.error(ex)
            return None
        finally:
            if mycursor is not None:
                mycursor.close()
            if connection is not None:
                connection.close()

    def fetch_list(self, sql, args=None):
        """Return a single list"""
        connection = None
        mycursor = None
        try:
            connection = self.get_connection()
            mycursor = connection.cursor()
            mycursor.execute(sql, args)
            results = mycursor.fetchall()
            return results
        except Exception as ex:
            logging.error(ex)
            return None
        finally:
            if mycursor is not None:
                mycursor.close()
            if connection is not None:
                connection.close()

    def fetch_record_sets(self, sql, args=None):
        """Return a single record_sets"""
        results = []
        connection = self.get_connection()
        mycursor = connection.cursor()
        result_sets = mycursor.execute(sql, args, multi=True)
        for result_set in result_sets:
            if result_set.with_rows:
                results.append(result_set.fetchall())
        mycursor.close()
        connection.close()
        return results

    def fetch_record_set(self, sql, args=None):
        """Return a first result_set in record_sets"""
        connection = None
        mycursor = None
        results = []
        try:
            connection = self.get_connection()
            mycursor = connection.cursor()
            result_sets = mycursor.execute(sql, args, multi=True)
            for result_set in result_sets:
                if result_set.with_rows:
                    results.append(result_set.fetchall())
            if len(results) > 0:
                return results[0]
            else:
                return []
        except Exception as ex:
            logging.error(ex)
            return None
        finally:
            if mycursor is not None:
                mycursor.close()
            if connection is not None:
                connection.close()
        

    def execute(self, sql, args=None):
        connection = None
        mycursor = None
        try:
            connection = self.get_connection()
            mycursor = connection.cursor()
            mycursor.execute(sql, args)
            connection.commit()
        except Exception as ex:
            logging.error(ex)
            return (-1, ex)
        finally:
            if mycursor is not None:
                mycursor.close()
            if connection is not None:
                connection.close()
        return (0, None) if mycursor is None else (mycursor.rowcount, None)

    def execute_many(self, sql, data_rows):
        connection = self.get_connection()
        mycursor = connection.cursor()
        mycursor.executemany(sql, data_rows)
        mycursor.close()
        connection.commit()
        connection.close()
        return mycursor.rowcount
        
    def execute_script(self, sql_script):
        connection = self.get_connection()
        mycursor = connection.cursor()
        result_sets = mycursor.execute(sql_script, None, multi=True)
        for result_set in result_sets:
            pass
        mycursor.close()
        connection.close()
        return mycursor.rowcount
        
    def execute_script_files_in_folder(self, scripts_folder_path):
        for dirpath, _, files in walk(scripts_folder_path):
            for file_name in files:
                script_file_path = path.join(dirpath, file_name)
                file_relative_path = path.relpath(script_file_path, scripts_folder_path)
                logging.info(f"Found file_relative_path [{file_relative_path}]")
                try:
                    # Load script
                    with open(script_file_path) as db_script_file:
                        sql_script = db_script_file.read()
                    # Run script
                    self.execute_script(sql_script)
                    logging.info(f"Executed {file_relative_path}")
                except Exception as e:
                    logging.error(e)

        