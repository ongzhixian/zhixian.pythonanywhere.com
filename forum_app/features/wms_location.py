from os import path
from forum_app import app_path
from forum_app.modules import app_state, log
from forum_app.features import BaseFeatureInterface, BaseMenuInterface

class WmsLocationFeature(BaseFeatureInterface):

    def __init__(self):
        super().__init__()

    @property
    def feature_name(self):
        """feature_name getter property. (required)"""
        return "WMS Location"

    @property
    def feature_description(self):
        """feature_description getter property. (required)"""
        return "Enable WMS Location module"

    def initialize(self):
        """Things to do when feature is initialized (eg. restore state from persistence storage) (on initialize_features)"""
        super().initialize()
        self.register()


    def register(self):
        if self.is_registered(self.feature_name):
            return
        # 
        # database_table_scripts_path = path.join(app_path, 'data', 'feature_database_scripts', 'wms', 'tables')
        # self.db.run_scripts_in_path(database_table_scripts_path)
        # Register featre 
        self.register_feature(self.feature_name, self.feature_description, __name__, "Warehouse Management System")

        # database_table_scripts_path = path.join(app_path, 'data', 'feature_database_scripts', 'wms', 'data')
        # self.db.run_scripts_in_path(database_table_scripts_path)
        # Add application menu item (if applicable)
        
        # BaseMenuInterface().add_menu_item(self.feature_name, 'WMS', 'Warehouse management module', '/wms/dashboard', 'Applications')


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

    def add(self, location_type_id, location_name, parent_location_id=None):
        sql = """insert into wms_location (location_type_id, name, parent_id) VALUES (%s, %s, %s);"""
        self.db.execute(sql, (location_type_id, location_name, parent_location_id))


    def get_location_type_list(self):
        sql = """
SELECT	id
        , name
FROM	wms_location_type
ORDER BY name;
"""
        return self.db.fetch_record_set(sql, None)

    def get_location_list(self):
        sql = """
SET @row_number = 0;
SELECT	(@row_number:=@row_number + 1) AS row_num
        , l.id AS 'location_id'
        , l.name AS 'location_name'
        , lt.name AS 'location_type_name'
from    wms_location l
inner join
        wms_location_type lt
        ON l.location_type_id = lt.id
LIMIT 25;
"""
        return self.db.fetch_record_set(sql, None)
