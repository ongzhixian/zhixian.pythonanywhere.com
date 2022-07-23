import os

import hashlib
import base64
import logging
import pdb


from forum_app.databases.mysql_data_provider import MySqlDataProvider

class User:
    def __init__(self):
        self.db = MySqlDataProvider('forum')

    def add(self, username, password):
        # Need to generate salt and hash
        password_salt = base64.b64encode(os.urandom(8))
        m = hashlib.sha256()

        salted_password = password_salt + password.encode("utf8")
        m.update(salted_password)
        password_hash = m.hexdigest()

        (rows_affected, error) = self.db.execute(
            "INSERT INTO login (username, password_salt, password_hash) VALUES (%s, %s, %s);", 
            (username, password_salt, password_hash))
        print(f"Rows affected {rows_affected}")
        error_message = None
        if rows_affected <= 0 and error is not None and error.errno == 1062:
            error_message = f"Username {username} already exists"
        return (rows_affected, error_message)

    def is_valid_credential(self, username, password):
        login_record = self.db.fetch_one(
            "SELECT username, password_hash, password_salt FROM `login` WHERE username = %s;", 
            (username,))
        if login_record is None:
            return False
        
        m = hashlib.sha256()
        stored_password_hash = login_record[1]
        stored_password_salt = login_record[2]
        salted_password = stored_password_salt.encode("utf8") + password.encode("utf8")
        m.update(salted_password)

        password_hash = m.hexdigest()
        return password_hash == stored_password_hash

    def get_user_logins(self):
        sql = """
SET @row_number = 0;
SELECT	(@row_number:=@row_number + 1) AS row_num
		, id
        , username
        , is_locked
FROM	login
ORDER BY username
LIMIT 25;
        """
        result_sets = self.db.fetch_record_sets(sql)
        if len(result_sets) > 0:
            logging.debug("result_sets: %s", result_sets)
            return result_sets[0]
        else:
            return []
        
