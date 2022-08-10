from os import path
from forum_app import app_path
from forum_app.modules import app_state, log
from forum_app.features import BaseFeatureInterface, BaseMenuInterface

class PracticeAccountFeature(BaseFeatureInterface):
    """Feature for setting up practice accounts"""

    def __init__(self):
        super().__init__()

    @property
    def feature_name(self):
        """feature_name getter property. (required)"""
        return "Practice Account"

    @property
    def feature_description(self):
        """feature_description getter property. (required)"""
        return "Enable practice accounts module"

    def initialize(self):
        """Things to do when feature is initialized (eg. restore state from persistence storage) (on initialize_features)"""
        super().initialize()
        self.register()


    def register(self):
        if self.is_registered(self.feature_name):
            return
        self.register_feature(self.feature_name, self.feature_description, __name__, 'Role-based access control') 
        # database_table_scripts_path = path.join(app_path, 'data', 'feature_database_scripts', 'practice_account', 'data')
        # self.db.run_scripts_in_path(database_table_scripts_path)
        # BaseMenuInterface().add_menu_item(self.feature_name, 'Practice Accounts', 'Practice account module', '/trade/dashboard', 'Applications')
        # What acocunts to setup when feature is registered
        from forum_app.features.login import LoginFeature
        from forum_app.features.role_based_access_control import RoleBasedAccessControlFeature
        login = LoginFeature()
        rbac = RoleBasedAccessControlFeature()
        login.add("admin1", "admin1")
        login.add("admin2", "admin2")

        login.add("dev1", "dev1")
        login.add("dev2", "dev2")

        login.add("tradeadmin1", "tradeadmin1")
        login.add("tradeadmin2", "tradeadmin2")
        login.add("tradeuser1", "tradeuser1")
        login.add("tradeuser2", "tradeuser2")
        rbac.assign_role("Trade user", "tradeuser1")
        rbac.assign_role("Trade user", "tradeuser2")
        rbac.assign_role("Trade administrator", "tradeadmin1")
        rbac.assign_role("Trade administrator", "tradeadmin2")

        # IPF users / RBAC
        
        login.add("ipfadmin1", "ipfadmin1")
        login.add("ipfadmin2", "ipfadmin2")
        rbac.assign_role("IPF administrator", "ipfadmin1")

        login.add("ipfuser1", "ipfuser1")
        login.add("ipfuser2", "ipfuser1")
        rbac.assign_role("IPF user", "ipfuser1")
        rbac.assign_role("IPF user", "ipfuser2")

        # WMS users / RBAC

        rbac.assign_role("WMS user", "dev1")
        rbac.assign_role("WMS administrator", "dev1")
        rbac.assign_role("Trade user", "dev1")
        rbac.assign_role("Trade administrator", "dev1")
        
        login.add("wmsadmin1", "wmsadmin1")
        login.add("wmsadmin2", "wmsadmin2")
        rbac.assign_role("WMS administrator", "wmsadmin1")
        # rbac.assign_role("WMS administrator", "wmsadmin2")

        login.add("wmscust1", "wmscust1")
        login.add("wmscust2", "wmscust2")
        rbac.assign_role("WMS customer", "wmscust1")
        rbac.assign_role("WMS customer", "wmscust2")

        # Refers to internal users 
        login.add("wmsuser1", "wmsuser1")
        login.add("wmsuser2", "wmsuser2")
        rbac.assign_role("WMS user", "wmsuser1")
        rbac.assign_role("WMS user", "wmsuser2")



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

