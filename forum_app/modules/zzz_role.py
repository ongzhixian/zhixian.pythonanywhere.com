import logging

from forum_app.databases.mysql_data_provider import MySqlDataProvider

class Role:
    def __init__(self):
        self.db = MySqlDataProvider('forum')

    def add(self, role_name):
        error_message = None

        (rows_affected, error) = self.db.execute("INSERT INTO role (role_name) VALUES (%s);", (role_name,))

        if error is not None:
            if error.errno == 1062:
                error_message = f"Role {role_name} already exists"
            else:
                error_message = error.msg
        
        return (rows_affected, error_message)

    def get_roles(self):
        sql = """
SET @row_number = 0;
SELECT	(@row_number:=@row_number + 1) AS row_num
		, id
        , name
FROM	role
ORDER BY name
LIMIT 25;
        """
        result_sets = self.db.fetch_record_sets(sql)
        if len(result_sets) > 0:
            logging.debug("result_sets: %s", result_sets)
            return result_sets[0]
        else:
            return []
        
