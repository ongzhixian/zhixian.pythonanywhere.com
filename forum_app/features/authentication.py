import logging
from forum_app.features import BaseFeatureInterface
from forum_app import app_state

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
        """Things to do when feature is initialized (on initialize_features)"""
        app_state['feature'][self.feature_name] = {
            "is_enable" : False
        }
        self.is_enable = False

    def register(self):
        if self.is_registered(self.feature_name):
            return
        self.register_feature(self.feature_name, self.feature_description, __name__)

    def load_app_settings(self, app_settings):
        logging.info(f"load_app_settings for {__name__}")
        is_enable = self.get_enable_setting()
        feature_settings = {}
        if __name__ in app_settings:
            app_settings[__name__] = {}
            feature_settings = app_settings[__name__]
        # 
        feature_settings["is_enable"] = is_enable
        # Update app_settings
        app_settings[__name__] = feature_settings
        

    def get_enable_setting(self):
        return super().get_enable_setting(__name__)
        # record = self.db.fetch_one(
        #     "SELECT is_enable FROM _feature WHERE module_name = %s;", 
        #     (__name__,))
        # if record is None:
        #     return False
        # return record[0] == 1

    def update_app_settings(self, app_settings):
        """Define/Set app_settings """
        print(__name__)
        if __name__ not in app_settings:
            app_settings[__name__] = {
                "is_enable": self.is_enable
            }
        
    def state_changed(self):
        """Signals a state changed event"""
        print("YA Auth state change")