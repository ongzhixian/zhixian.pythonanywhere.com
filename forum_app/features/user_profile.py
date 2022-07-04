from forum_app.features import BaseFeatureInterface

class UserProfileFeature(BaseFeatureInterface):
    def __init__(self):
        super().__init__()

    def register(self):
        feature_name = "UserProfile"
        feature_description = "Enable user profile module"
        
        if self.is_registered(feature_name):
            return

        self.register_feature(feature_name, feature_description)
