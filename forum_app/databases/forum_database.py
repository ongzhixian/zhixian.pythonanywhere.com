import logging
import pdb

from forum_app.databases import BaseDatabaseInterface
from forum_app.databases.mysql_data_provider import MySqlDataProvider


class ForumDatabase(BaseDatabaseInterface):
    def __init__(self):
        self.db = MySqlDataProvider('forum')

    def create_database_if_not_exists(self):
        """Create database if not exists"""
        self.db.create_database_if_not_exists()
        return

