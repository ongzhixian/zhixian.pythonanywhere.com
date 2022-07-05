import logging
import os
from forum_app import app_path
from forum_app.features import BaseFeatureInterface

class RbacFeature(BaseFeatureInterface):
    def __init__(self):
        super().__init__()

    def register(self):
        feature_name = "Role-based access control"
        feature_description = "Enable role-based access control module"
        
        if self.is_registered(feature_name):
            return

        self.register_feature(feature_name, feature_description, __name__)

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
