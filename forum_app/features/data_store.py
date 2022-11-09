from pymongo import MongoClient

from forum_app.features.logging import log

class DataStore(object):
    def __new__(cls, *args):
        if hasattr(cls, 'instance'):
            log.debug("Reuse datastore instance")
            return cls.instance

        log.debug("Create datastore instance")
        cls.instance = super(DataStore, cls).__new__(cls)
        return cls.instance

    def __init__(self, app_state):
        if app_state is None:
            raise ValueError("app_state", "is None")

        self.app_state = app_state

        # if mongodb_connection_string is not None:
        #     log.debug("Initialize wiki")
        #     self.mongodb_connection_string = mongodb_connection_string
        #     mongodb = MongoDb(self.mongodb_connection_string, self.WIKI_DATABASE_NAME)
        #     self.init_wiki_collection(mongodb)

    def __getitem__(self, indexer):
        return "my item"