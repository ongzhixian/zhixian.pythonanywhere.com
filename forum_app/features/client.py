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

    def add_new(self, client_name_field, client_type_id=0):
        """Add a new client"""
        rows_affected = self.db.execute(
            "INSERT INTO client (name, type_id) VALUES (%s, %s);", 
            (client_name_field, client_type_id))
        print(f"Rows affected {rows_affected}")
        return rows_affected

    def get_client_list(self, client_name='', type_id=0):
        sql = """
SET @row_number = 0;
SELECT	(@row_number:=@row_number + 1) AS row_num
		, id
        , name
FROM	client
WHERE   name LIKE %s 
        AND type_id = %s
ORDER BY name
LIMIT 25;
        """
        result_sets = self.db.fetch_record_sets(sql, (f"%{client_name}%", type_id))
        if len(result_sets) > 0:
            return result_sets[0]
        else:
            return []

    def get_client_type_list(self):
        records = self.db.fetch_list("SELECT id, name FROM client_type ORDER BY name;", None)
        if records is None:
            return []
        return records