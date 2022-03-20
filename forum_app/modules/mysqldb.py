import logging as log

from os import environ

from forum_app import app, secrets
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

    def getDatabase(self):
        mydb = mysql.connector.connect(
            host=self.db_settings['HOST'],
            user=self.db_settings['USERNAME'],
            password=self.db_settings['PASSWORD'],
            database=self.db_settings['DATABASE']
        )
        mycursor = mydb.cursor()

        mycursor.execute("SHOW DATABASES")

        for x in mycursor:
            print(x)
    
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
