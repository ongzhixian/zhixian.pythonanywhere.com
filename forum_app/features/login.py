from forum_app.features import BaseFeatureInterface

class LoginFeature(BaseFeatureInterface):
    def __init__(self):
        super().__init__()

    def register(self):
        feature_name = "Login"
        feature_description = "Enable login module"
        
        if self.is_registered(feature_name):
            return

        self.register_feature(feature_name, feature_description, __name__)
