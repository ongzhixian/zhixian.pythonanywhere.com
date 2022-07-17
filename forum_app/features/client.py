from forum_app.modules import app_state, log
from forum_app.features import BaseFeatureInterface
from forum_app.databases.mysql_data_provider import MySqlDataProvider

class ClientFeature(BaseFeatureInterface):

    def __init__(self):
        super().__init__()
        self.db = MySqlDataProvider('forum')

    @property
    def feature_name(self):
        """feature_name getter property. (required)"""
        return "Client"

    @property
    def feature_description(self):
        """feature_description getter property. (required)"""
        return "Enable client module"

    def initialize(self):
        """Things to do when feature is initialized (eg. restore state from persistence storage) (on initialize_features)"""
        super().initialize()
        self.register()


    def register(self):
        if self.is_registered(self.feature_name):
            return
        self.register_feature(self.feature_name, self.feature_description, __name__)


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


    # Feature specific functions below

    def add_new(self, first_name_field, last_name_field):
        """Add a new client"""
        # from databases.mysql_data_provider import MySqlDataProvider
        # db = MySqlDataProvider('forum')

        # rows_affected = self.db.execute(
        #     "INSERT INTO login (username, password_salt, password_hash) VALUES (%s, %s, %s);", 
        #     (username, password_salt, password_hash))
        # print(f"Rows affected {rows_affected}")
        # return rows_affected
        pass