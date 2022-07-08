import logging
from functools import wraps
from flask import redirect, url_for, g, request
from forum_app.features import BaseFeatureInterface, is_feature_enable
from forum_app import add_menu_item, remove_menu_item

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


    def register(self):
        if self.is_registered(self.feature_name):
            return
        self.register_feature(self.feature_name, self.feature_description, __name__)

        
    def app_state_changed(self, app_state, event_data=None):
        """Things to do whenever app_state changed"""
        # We want to selective add/remove logins menu item to admin menu in drawer
        logging.debug(f"{self.feature_name} is_enable: {self.is_enable}")
        if self.is_enable:
            logging.debug("Add to drawer_admin_menu")
            add_menu_item('drawer_admin_menu', ("Logins", "/sample/login-item", "table_rows", "logins-menu-item"))
        else:
            # Remove login menu item to admin menu in drawer
            logging.debug("Remove drawer_admin_menu")
            remove_menu_item('drawer_admin_menu', 'logins-menu-item')
            

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