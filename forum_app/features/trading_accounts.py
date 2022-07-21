from forum_app.modules import app_state, log
from forum_app.features import BaseFeatureInterface

class TradingAccountFeature(BaseFeatureInterface):

    def __init__(self):
        super().__init__()

    @property
    def feature_name(self):
        """feature_name getter property. (required)"""
        return "Trading Account"

    @property
    def feature_description(self):
        """feature_description getter property. (required)"""
        return "Enable trading account module"

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

    # Feature specific methods

#     def get_portfolio_list(self):
#         sql = """
# SET @row_number = 0;
# SELECT	(@row_number:=@row_number + 1) AS row_num
# 		, id
# FROM	portfolio
# ORDER BY id
# LIMIT 25;
#         """
#         result_sets = self.db.fetch_record_sets(sql, None)
#         if len(result_sets) > 0:
#             return result_sets[0]
#         else:
#             return []
