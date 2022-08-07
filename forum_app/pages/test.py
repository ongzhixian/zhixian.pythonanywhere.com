import logging as log
from flask import render_template, request
from forum_app import app
# from forum_app.modules.ZZZ_sqlitedb import SqliteDatabase

@app.route('/test/')
def test_get():
    """Web page at '/'"""
    #return app.config
    return render_template('test_get.html')

@app.route('/test/add')
def test_add_get():
    """Web page at '/'"""
    #return app.config
    return render_template('test_add_get.html')

@app.route('/test/add', methods=['POST'])
def test_add_post():
    """Web page at '/'"""

    topic_title     = request.form['topic_title']
    topic_content   = request.form['topic_content']

    #create_database()
    #create_table()
    #add_record(topic_title, topic_content)
    try:
        db = SqliteDatabase('./forum_app/data/xxxforums.db')
        db.execute("INSERT INTO test_topic (title, content) values (?, ?);", topic_title, topic_content)
    except Exception as ex:
        log.error(f"[{ex}];")

    log.info(f"topic_title is {topic_title}")
    log.info(f"topic_content is {topic_content}")

    return render_template('test_add_get.html')


@app.route('/test/init')
def test_init_get():
    """Web page at '/test/init'"""
#     try:
#         db = SqliteDatabase('./forum_app/data/xxxforums.db')
#         db.create_database()
#         db.create_table("""CREATE TABLE "test_topic" (
# 	"id"	INTEGER PRIMARY KEY AUTOINCREMENT,
# 	"title"	TEXT NOT NULL UNIQUE,
# 	"content"	TEXT NOT NULL,
# 	"cre_dt"	TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
# 	"upd_dt"	TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
# );""")  
#     except Exception as ex:
#         log.error(f"[{ex}];")
    return render_template('test_add_get.html')



# @app.route('/test/add', methods=['POST'])
# def test_init_post():
#     """Web page at '/'"""

#     topic_title     = request.form['topic_title']
#     topic_content   = request.form['topic_content']

#     log.info(f"topic_title is {topic_title}")
#     log.info(f"topic_content is {topic_content}")

#     return render_template('test_add_get.html')

def create_database():
    import sqlite3
    import os
    try:
        #con = sqlite3.connect('./forum_app/data/example.db')
        #db_path = './data/forums.db'
        db_path = './forum_app/data/forums.db'
        with sqlite3.connect(db_path) as db:
            cur = db.cursor()
    except sqlite3.OperationalError as ex:
        log.error(f"[{ex}]; Trying to open [{db_path}] from [{os.getcwd()}]")
    except Exception as ex:
        log.error(f"[{ex}];")

def create_table():
    import sqlite3
    import os
    sql = """CREATE TABLE "test_topic" (
	"id"	INTEGER PRIMARY KEY AUTOINCREMENT,
	"title"	TEXT NOT NULL UNIQUE,
	"content"	TEXT NOT NULL,
	"cre_dt"	TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
	"upd_dt"	TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
);"""
    try:
        db_path = './forum_app/data/forums.db'
        with sqlite3.connect(db_path) as db:
            cur = db.cursor()
            cur.execute(sql)
            db.commit()
    except sqlite3.OperationalError as ex:
        log.error(f"[{ex}]; Trying to open [{db_path}] from [{os.getcwd()}]")
    except Exception as ex:
        log.error(f"[{ex}];")
    pass

def add_record(title, content):
    import sqlite3
    import os
    # cur.execute("insert into people values (?, ?)", (who, age))
    sql = "INSERT INTO test_topic values (?, ?);"
    try:
        db_path = './forum_app/data/forums.db'
        with sqlite3.connect(db_path) as db:
            cur = db.cursor()
            cur.execute("INSERT INTO test_topic (title, content) values (?, ?);", (title, content))
            db.commit()
    except sqlite3.OperationalError as ex:
        log.error(f"[{ex}]; Trying to open [{db_path}] from [{os.getcwd()}]")
    except Exception as ex:
        log.error(f"[{ex}];")
    pass



def get_database(database_type, connection_string):
    pass

# class DatabaseInterface():
#     def __init__(self, connection_string):
#         self.connection_string = connection_string
    
#     def create_database(self):
#         pass

#     def create_table(self, sql):
#         pass

#     def execute(self, sql, values):
#         pass

# class SqliteDatabase():
#     def __init__(self, connection_string):
#         self.connection_string = connection_string
    
#     def create_database(self):
#         pass

#     def create_table(self, sql):
#         pass

#     def execute(self, sql, values):
#         pass

