import logging as log

from os import environ

from forum_app import secrets

import mysql.connector

# def create_database(db_path):
#     try:
#         with sqlite3.connect(db_path) as db:
#             cur = db.cursor()
#     except sqlite3.OperationalError as ex:
#         log.error(f"[{ex}]; Trying to open [{db_path}] from [{os.getcwd()}]")
#     except Exception as ex:
#         log.error(f"[{ex}];")

class MySqlDatabase:
    def __init__(self, database_name):
        prefix = ''
        if 'PYTHONANYWHERE_DOMAIN' not in environ:
            prefix = 'dev_'
        setting_name = f'{prefix}{database_name}'
        
        log.info(f"Init {database_name} using {setting_name} settings")
        self.db_settings = secrets['MYSQL'][setting_name]

    def get_connection(self):
        mydb = mysql.connector.connect(
            host=self.db_settings['HOST'],
            port=self.db_settings['PORT'],
            user=self.db_settings['USERNAME'],
            password=self.db_settings['PASSWORD'],
            database=self.db_settings['DATABASE']
        )
        return mydb


    def fetch_one(self, sql, args):
        # With statements does not work on Python 3.7 :-(
        # with self.get_connection() as connection, connection.cursor() as mycursor:
        #     mycursor.execute(sql)
        #     return mycursor.fetchone()
        # The Python 3.7 compliant way
        connection = self.get_connection()
        mycursor = connection.cursor()
        mycursor.execute(sql, args)
        return mycursor.fetchone()


    def fetch_all(self, sql, args=None):
        # With statements does not work on Python 3.7 :-(
        # with self.get_connection() as connection, connection.cursor() as mycursor:
        #     mycursor.execute(sql)
        #     return mycursor.fetchone()
        # The Python 3.7 compliant way
        connection = self.get_connection()
        mycursor = connection.cursor()
        mycursor.execute(sql, args)
        return mycursor.fetchall()


    def table_exists(self, table_name):
        sql = """SELECT 1 FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_TYPE = 'BASE TABLE' AND TABLE_NAME = %s;"""
        # With statements does not work on Python 3.7 :-(
        # with self.get_connection() as connection, connection.cursor() as mycursor:
        #     mycursor.execute(sql, (table_name,))
        #     return False if mycursor.fetchone() == None else True
        # The Python 3.7 compliant way
        connection = self.get_connection()
        mycursor = connection.cursor()
        mycursor.execute(sql, (table_name,))
        return False if mycursor.fetchone() == None else True


    def create_table(self, sql):
        # With statements does not work on Python 3.7 :-(
        # with self.get_connection() as connection, connection.cursor() as mycursor:
        #     mycursor.execute(sql)
        # The Python 3.7 compliant way
        connection = self.get_connection()
        mycursor = connection.cursor()
        mycursor.execute(sql)


    def execute(self, sql, args = None):
        # With statements does not work on Python 3.7 :-(
        # with self.get_connection() as connection, connection.cursor() as mycursor:
        #     mycursor.execute(sql, args)
        #     connection.commit()
        #     return mycursor.rowcount
        # The Python 3.7 compliant way
        connection = self.get_connection()
        mycursor = connection.cursor()
        mycursor.execute(sql, args)
        # connection.commit()
        return mycursor.rowcount

    def execute_batch(self, sql, data):
        # With statements does not work on Python 3.7 :-(
        # with self.get_connection() as connection, connection.cursor() as mycursor:
        #     mycursor.executemany(sql, data)
        #     connection.commit()
        #     return mycursor.rowcount
        # The Python 3.7 compliant way
        connection = self.get_connection()
        mycursor = connection.cursor()
        mycursor.executemany(sql, data)
        # connection.commit()
        return mycursor.rowcount
            
    
    # def create_database(self):
    #     try:
    #         log.info(f"connection_string=[{self.connection_string}]")
    #         with sqlite3.connect(self.connection_string) as db:
    #             cur = db.cursor()
    #     except sqlite3.OperationalError as ex:
    #         log.error(f"[{ex}]; Trying to open [{self.connection_string}] from [{os.getcwd()}]")
    #     except Exception as ex:
    #         log.error(f"[{ex}];")


    # def create_table(self, sql):
    #     log.info(f"sql=[{sql}]")
    #     try:
    #         with sqlite3.connect(self.connection_string) as db:
    #             cur = db.cursor()
    #             cur.execute(sql)
    #             db.commit()
    #     except sqlite3.OperationalError as ex:
    #         log.error(f"[{ex}]; Trying to open [{self.connection_string}] from [{os.getcwd()}]")
    #     except Exception as ex:
    #         log.error(f"[{ex}];")


    # def execute(self, sql, *values):
    #     log.info(f"sql=[{sql}], values=[{values}]")
    #     try:
    #         with sqlite3.connect(self.connection_string) as db:
    #             cur = db.cursor()
    #             cur.execute(sql, values)
    #             db.commit()
    #     except sqlite3.OperationalError as ex:
    #         log.error(f"[{ex}]; Trying to open [{self.connection_string}] from [{os.getcwd()}]")
    #     except Exception as ex:
    #         log.error(f"[{ex}];")
    #     pass
