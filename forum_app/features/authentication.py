from forum_app.features import BaseFeatureInterface
import pdb
class AuthenticationFeature(BaseFeatureInterface):

    def __init__(self):
        super().__init__()

    def register(self):
        feature_name = "Authentication"
        feature_description = "Enables authentication module"
        
        if self.is_registered(feature_name):
            return

        self.register_feature(feature_name, feature_description)

    def load_app_settings(self, app_settings):
        self.get_enable_setting()
        pass

    def get_enable_setting():
        pass

    def update_app_settings(self, app_settings):
        """Define/Set app_settings """
        print(__name__)
        if __name__ not in app_settings:
            app_settings[__name__] = {
                "is_enable": self.is_enable
            }
        