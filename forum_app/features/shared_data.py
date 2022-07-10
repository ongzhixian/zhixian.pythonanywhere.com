import logging

# from forum_app import add_menu_item, remove_menu_item
from forum_app.features import BaseFeatureInterface

class SharedDataFeature(BaseFeatureInterface):

    def __init__(self):
        super().__init__()

    @property
    def feature_name(self):
        """feature_name getter property. (required)"""
        return "Shared data"

    @property
    def feature_description(self):
        """feature_description getter property. (required)"""
        return "Enable shared data module"

    def initialize(self):
        """Things to do when feature is initialized (eg. restore state from persistence storage) (on initialize_features)"""
        super().initialize()


    def register(self):
        if self.is_registered(self.feature_name):
            return
        self.register_feature(self.feature_name, self.feature_description, __name__)


    def app_state_changed(self, app_state, event_data=None):
        """Things to do whenever app_state changed"""
        if not self.is_my_event(event_data):
            return
        menu_item_id = "shared-data-menu-item"
        # We want to selective add/remove logins menu item to admin menu in drawer
        logging.debug(f"{self.feature_name} is_enable: {self.is_enable}")
        if self.is_enable:
            logging.debug("Add to drawer_admin_menu")
            # add_menu_item('drawer_admin_menu', ("Shared Data", "/shared-data/dashboard", "table_rows", menu_item_id))
        else:
            # Remove login menu item to admin menu in drawer
            logging.debug("Remove drawer_admin_menu")
            # remove_menu_item('drawer_admin_menu', menu_item_id)