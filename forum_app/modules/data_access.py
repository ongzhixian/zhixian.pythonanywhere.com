import logging as log
import os
import sqlite3

# def create_database(db_path):
#     try:
#         with sqlite3.connect(db_path) as db:
#             cur = db.cursor()
#     except sqlite3.OperationalError as ex:
#         log.error(f"[{ex}]; Trying to open [{db_path}] from [{os.getcwd()}]")
#     except Exception as ex:
#         log.error(f"[{ex}];")

class SqliteDatabase():
    def __init__(self, connection_string):
        log.info(f"Init {connection_string}")
        self.connection_string = connection_string
    
    def create_database(self):
        try:
            log.info(f"connection_string=[{self.connection_string}]")
            with sqlite3.connect(self.connection_string) as db:
                cur = db.cursor()
        except sqlite3.OperationalError as ex:
            log.error(f"[{ex}]; Trying to open [{self.connection_string}] from [{os.getcwd()}]")
        except Exception as ex:
            log.error(f"[{ex}];")


    def create_table(self, sql):
        log.info(f"sql=[{sql}]")
        try:
            with sqlite3.connect(self.connection_string) as db:
                cur = db.cursor()
                cur.execute(sql)
                db.commit()
        except sqlite3.OperationalError as ex:
            log.error(f"[{ex}]; Trying to open [{self.connection_string}] from [{os.getcwd()}]")
        except Exception as ex:
            log.error(f"[{ex}];")


    def execute(self, sql, *values):
        log.info(f"sql=[{sql}], values=[{values}]")
        try:
            with sqlite3.connect(self.connection_string) as db:
                cur = db.cursor()
                cur.execute(sql, values)
                db.commit()
        except sqlite3.OperationalError as ex:
            log.error(f"[{ex}]; Trying to open [{self.connection_string}] from [{os.getcwd()}]")
        except Exception as ex:
            log.error(f"[{ex}];")
        pass
