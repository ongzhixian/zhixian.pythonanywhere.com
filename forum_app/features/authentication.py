from forum_app.features import BaseFeatureInterface

class AuthenticationFeature(BaseFeatureInterface):
    def __init__(self):
        super().__init__()

    def register(self):
        feature_name = "Authentication"
        feature_description = "Enables authentication module"
        
        if self.is_registered(feature_name):
            return

        self.register_feature(feature_name, feature_description)
