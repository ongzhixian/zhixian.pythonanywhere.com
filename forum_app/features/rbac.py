import logging
import os
from forum_app import app_path, app_state
from forum_app.features import BaseFeatureInterface

class RbacFeature(BaseFeatureInterface):
    def __init__(self):
        super().__init__()

    @property
    def feature_name(self):
        """feature_name getter property. (required)"""
        return "Role-based access control"

    @property
    def feature_description(self):
        """feature_description getter property. (required)"""
        return "Enable role-based access control module"

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

        # Run table scripts (if any)
        DB_SCRIPTS_PATH = os.path.join(app_path, 'data', 'feature_database_scripts', "login")
        self.db.execute_script_files_in_folder(DB_SCRIPTS_PATH)
        # for dirpath, _, files in os.walk(DB_SCRIPTS_PATH):
        #     for file_name in files:
        #         script_file_path = os.path.join(dirpath, file_name)
        #         file_relative_path = os.path.relpath(script_file_path, DB_SCRIPTS_PATH)
        #         logging.info(f"Found file_relative_path [{file_relative_path}]")
        #         try:
        #             # Load script
        #             with open(script_file_path) as db_script_file:
        #                 sql_script = db_script_file.read()
        #             # Run script
        #             self.db.execute_script(sql_script)
        #             logging.info(f"Executed {file_relative_path}")
        #         except Exception as e:
        #             logging.info("Some error occurred", e)
