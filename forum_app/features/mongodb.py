import logging

from pymongo import MongoClient

# def test_connect(connection_string):
#     logging.info(f"ConnectionString is: {connection_string}")
#     mongo_client = MongoClient(connection_string)
#     print(mongo_client.list_database_names())
#     db = mongo_client['minitools']
#     print(db.list_collection_names())

class MongoDb(object):
    def __init__(self, connection_string, database_name):
        self.connection_string = connection_string
        self.database_name = database_name
        self.database_names = []
        self.refresh_database_names()
        
    # def test_connectivity(self):
    #     mongo_client = MongoClient(self.connection_string)
    #     print(mongo_client.list_database_names())
    #     db = mongo_client['minitools']
    #     print(db.list_collection_names())

    def refresh_database_names(self):
        mongo_client = MongoClient(self.connection_string)
        self.database_names = mongo_client.list_database_names()

    def get_database(self):
        mongo_client = MongoClient(self.connection_string)
        if self.database_name in self.database_names:
            logging.info("Database exists.")
            return mongo_client[self.database_name]
        logging.error(f"'{self.database_name}' not found. Available databases are {self.database_names}")
        raise ValueError(self.database_name, "not found")

    def collection_exists(self, collection_name):
        db = self.get_database()
        collection_names = db.list_collection_names()
        return collection_name in collection_names

    def get_collection(self, collection_name):
        db = self.get_database()
        return db[collection_name]