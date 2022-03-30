from os import environ

from forum_app import app, secrets

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

    def init_new_tables(self):
        if not self.db.table_exists('weblink'): self.db.create_table(self.sql_create_weblink)
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