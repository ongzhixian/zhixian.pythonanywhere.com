import logging
from os import path
from functools import wraps
from flask import redirect, url_for, g, request
from forum_app import app_path
from forum_app.features import BaseFeatureInterface, is_feature_enable
from forum_app.pages import menu
from forum_app.modules import app_state, log

import pdb

class AuthenticationFeature(BaseFeatureInterface):

    def __init__(self):
        super().__init__()

    @property
    def feature_name(self):
        """feature_name getter property. (required)"""
        return "Authentication"

    @property
    def feature_description(self):
        """feature_description getter property. (required)"""
        return "Enables authentication module"

    def initialize(self):
        """Things to do when feature is initialized (eg. restore state from persistence storage) (on initialize_features)"""
        super().initialize()
        self.register()


    def register(self):
        if self.is_registered(self.feature_name):
            return
        database_table_scripts_path = path.join(app_path, 'data', 'feature_database_scripts', 'login', 'tables')
        self.db.run_scripts_in_path(database_table_scripts_path)
        self.register_feature(self.feature_name, self.feature_description, __name__)

        
    def app_state_changed(self, event_data=None):
        """Things to do whenever app_state changed"""
        is_my_event = self.is_my_event(event_data)
        # log.debug(f"is_my_event {is_my_event}")
        if not self.is_my_event(event_data):
            return

        # We want to selective add/remove logins menu item to admin menu in drawer
        authentication_login_menu_item_id = "authentication-logins"
        log.debug(f"{self.feature_name} is_enable: {self.is_enable} event_data {event_data}")
        if self.is_enable:
            logging.debug("Add to drawer_admin_menu")
            app_state.add_to_menu('drawer_admin_menu', 
                authentication_login_menu_item_id, "Logins", "/user/dashboard", False, "table_rows",)
        else:
            # Remove login menu item to admin menu in drawer
            logging.debug("Remove drawer_admin_menu")
            app_state.remove_from_menu('drawer_admin_menu', 
                authentication_login_menu_item_id)
            

    # def load_app_settings(self, app_settings):
    #     logging.info(f"load_app_settings for {__name__}")
    #     is_enable = self.get_enable_setting()
    #     feature_settings = {}
    #     if __name__ in app_settings:
    #         app_settings[__name__] = {}
    #         feature_settings = app_settings[__name__]
    #     # 
    #     feature_settings["is_enable"] = is_enable
    #     # Update app_settings
    #     app_settings[__name__] = feature_settings
        

    # def get_enable_setting(self):
    #     return super().get_enable_setting(__name__)
    #     # record = self.db.fetch_one(
    #     #     "SELECT is_enable FROM _feature WHERE module_name = %s;", 
    #     #     (__name__,))
    #     # if record is None:
    #     #     return False
    #     # return record[0] == 1

    # def update_app_settings(self, app_settings):
    #     """Define/Set app_settings """
    #     print(__name__)
    #     if __name__ not in app_settings:
    #         app_settings[__name__] = {
    #             "is_enable": self.is_enable
    #         }


# Decorators defined 

def authentication_check(f):
    @wraps(f)
    def authentication_check_wrap(*args, **kwargs):
        is__authentication_feature_enable = is_feature_enable("Authentication")
        logging.debug(f"is__authentication_feature_enable: {is__authentication_feature_enable}")
        if not is__authentication_feature_enable:
            return f(*args, **kwargs)
        # Else authentication feature is enabled, and then we should check...
        if 'username' in g:
            logging.debug(f"Is valid user: {g.username}")
            return f(*args, **kwargs)
        else:
            logging.debug(f"Is anonymous user")
            return redirect(url_for('login', next=request.url))
    return authentication_check_wrap