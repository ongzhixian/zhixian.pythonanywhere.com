import os
import logging

from forum_app.modules.mysqldb import MySqlDatabase

class ForumDb:
    def __init__(self):
        self.db = MySqlDatabase('forum')
        self.sqlMap = {
            'create_weblink': ForumDb.sql_create_weblink
        }
        # self.tables = {
        #     'weblink': {
        #         'exists_script': ForumDb.sql_exists_weblink,
        #         'create_script': ForumDb.sql_create_weblink
        #     },
        #     #'table_version': {}
        # }
        # self.init_new_tables()

    def one_time_initialization(self, app_path):
        # Discover scripts to run in data/database_init_scripts
        # /home/zhixian/website/run/forum_app/data/database_init_scripts
        # /home/zhixian/website/run/forum_app/data/database_init_scripts

        DB_SCRIPTS_PATH = os.path.join(app_path, 'data', 'database_init_scripts')

        logging.info(f"Discovering database scripts in {DB_SCRIPTS_PATH}")

        # self.db.execute("CREATE TABLE TestTable (`id` INT UNSIGNED NOT NULL, `message` VARCHAR(50) DEFAULT '')")

        for dirpath, _, files in os.walk(DB_SCRIPTS_PATH):
            for file_name in files:
                script_file_path = os.path.join(dirpath, file_name)
                file_relative_path = os.path.relpath(script_file_path, DB_SCRIPTS_PATH)
                logging.info(f"Found file_relative_path [{file_relative_path}]")
                # Load script
                with open(script_file_path) as db_script_file:
                    sql_script = db_script_file.read()
                # Run script
                # logging.info(sql_script)
                self.db.execute_script(sql_script)
                logging.info(f"Executed {file_relative_path}")
        

    def init_new_tables(self):
        pass
        #if not self.db.table_exists('weblink'): self.db.create_table(self.sql_create_weblink)
        #print('weblink2 table exists1') if self.db.table_exists('asdweblink2') else print('weblink2 table NOT exists')
        #print(f"result {result}")
        # for (table_name, scripts) in self.tables:
        #     if not self.db.execute_sql(scripts['exists_script']):
        #         self.db.execute_sql(scripts['create_script'])

    def get_database(self):
        mydb = self.db.getDatabase()
        mycursor = mydb.cursor()
        mycursor.execute("SHOW DATABASES")
        for x in mycursor:
            print(x)
    
    def add_weblink(self, url):
        print("Executing add_weblink")
        rows_affected = self.db.execute(
            "INSERT INTO weblink (url) VALUES (%s);", (url,))
        print(f"Rows affected {rows_affected}")

    def add_weblinks(self, url_list):
        print("Executing add_weblink")
        rows_affected = self.db.execute_batch(
            "INSERT INTO weblink (url) VALUES (%s);", url_list)
        print(f"Rows affected {rows_affected}")

    def add_db_migrate(self, file_path):
        rows_affected = self.db.execute(
            "INSERT INTO _db_migrate (file_path) VALUES (%s);", (file_path,))
        logging.info(f"add_db_migrate (rows affected): [{rows_affected}]")
        
    def db_migrate_exists(self, file_path):
        record = self.db.fetch_one(
            "SELECT 1 FROM _db_migrate WHERE file_path = %s;", (file_path,))
        record_exists = record is not None
        logging.info(f"db_migrate_exists: [{record_exists}]")
        return record_exists

    def get_unapplied_db_migrate_count(self):
        record = self.db.fetch_one(
            "SELECT COUNT(id) AS 'COUNT' FROM _db_migrate WHERE apply_dt IS NULL;", None)
        return record[0]

    def get_unapplied_db_migrate_list(self):
        records = self.db.fetch_all(
            "SELECT id, file_path, cre_dt FROM _db_migrate WHERE apply_dt IS NULL;", None)
        return records

    def get_schema_object_count(self):
        record = self.db.fetch_one(
            "SELECT table_count, view_count, procedure_count, function_count FROM schema_object_count;", None)
        return record

    def myfunc(self, a):
        return {
            'a': a[0],
            'b': a[1]
        }

    def get_links_added_by_date(self):
        data = self.db.fetch_all(
            """
WITH dt AS
(
	SELECT COUNT(url) AS 'count', DATE(created_dt) AS 'created_dt' FROM weblink
	GROUP BY DATE(created_dt)
	ORDER BY DATE(created_dt) DESC
  	LIMIT 5
 )
 SELECT * FROM dt ORDER BY created_dt
""")
        return list(map(lambda d : {'count':d[0], 'date':d[1]}, data))

    # Sql create table scripts

    sql_create_weblink = """
CREATE TABLE `weblink` (
	`id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
	`url` VARCHAR(2048) NOT NULL,
	`created_dt` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP(),
	PRIMARY KEY (`id`)
)
COLLATE='utf8mb4_general_ci'
;
"""