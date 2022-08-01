import hashlib
import base64
from os import path, urandom
from forum_app import app_path
from forum_app.modules import app_state, log
from forum_app.features import BaseFeatureInterface

class LoginFeature(BaseFeatureInterface):

    def __init__(self):
        super().__init__()

    @property
    def feature_name(self):
        """feature_name getter property. (required)"""
        return "Login"

    @property
    def feature_description(self):
        """feature_description getter property. (required)"""
        return "Enable login module"

    def initialize(self):
        """Things to do when feature is initialized (eg. restore state from persistence storage) (on initialize_features)"""
        super().initialize()
        self.register()


    def register(self):
        if self.is_registered(self.feature_name):
            return
        database_table_scripts_path = path.join(app_path, 'data', 'feature_database_scripts', 'login', 'tables')
        self.db.run_scripts_in_path(database_table_scripts_path)
        database_table_scripts_path = path.join(app_path, 'data', 'feature_database_scripts', 'login', 'views')
        self.db.run_scripts_in_path(database_table_scripts_path)
        self.register_feature(self.feature_name, self.feature_description, __name__, "Authentication")

    def update_ui(self):
        # We want to selective add/remove logins menu item to admin menu in drawer
        # menu_item_id = "shared-data-dashboard"
        #
        # if self.is_enable:
        #     logging.debug("Add to drawer_admin_menu")
        #     app_state.add_to_menu('drawer_admin_menu', menu_item_id, "Shared data", "/shared-data/dashboard", False, "table_rows",)
        # else:
        #     # Remove login menu item to admin menu in drawer
        #     logging.debug("Remove drawer_admin_menu")
        #     app_state.remove_from_menu('drawer_admin_menu', menu_item_id)
        pass

    def app_state_changed(self, event_data=None):
        """Things to do whenever app_state changed"""
        if not self.is_my_event(event_data):
            return
        log.debug(f"{self.feature_name} is_enable: {self.is_enable} event_data {event_data}")
        self.update_ui()

    # Feature specific methods

    def add(self, username, password):
        """Add new user with username and password"""
        # Need to generate salt and hash

        password_salt = base64.b64encode(urandom(8))
        m = hashlib.sha256()

        salted_password = password_salt + password.encode("utf8")
        m.update(salted_password)
        password_hash = m.hexdigest()

        (rows_affected, error) = self.db.execute(
            "INSERT INTO login (username, password_salt, password_hash) VALUES (%s, %s, %s);", 
            (username, password_salt, password_hash))
        print(f"Rows affected {rows_affected}")
        return rows_affected

    def is_valid_credential(self, username, password):
        login_record = self.db.fetch_record(
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

    def get_users(self):
        sql = """
SET @row_number = 0;
SELECT	(@row_number:=@row_number + 1) AS row_num
		, id
        , username
FROM	login
ORDER BY username
LIMIT 25;
        """
        result_sets = self.db.fetch_record_sets(sql)
        if len(result_sets) > 0:
            return result_sets[0]
        else:
            return []
        