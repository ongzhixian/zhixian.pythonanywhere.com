from pymongo import ASCENDING
from forum_app.features.logging import log
from forum_app.features.mongodb import MongoDb

class Wiki(object):
    def __new__(cls, mongodb_connection_string=None):
        if not hasattr(cls, 'instance'):
            log.debug("Create wiki instance")
            cls.instance = super(Wiki, cls).__new__(cls)
            cls.mongodb_connection_string = mongodb_connection_string
            mongodb = MongoDb(mongodb_connection_string, cls.WIKI_DATABASE_NAME)
            cls.init_wiki_collection
        log.debug("Reuse wiki instance")
        return cls.instance

    def __init__(self, mongodb_connection_string=None):
        self.WIKI_DATABASE_NAME = 'minitools'
        self.WIKI_COLLECTION_NAME = 'wiki'
        # if mongodb_connection_string is not None:
        #     self.mongodb_connection_string = mongodb_connection_string
        #     mongodb = MongoDb(self.mongodb_connection_string, self.WIKI_DATABASE_NAME)
        #     self.init_wiki_collection(mongodb)

    def init_wiki_collection(self, mongodb):
        if mongodb.collection_exists(self.WIKI_COLLECTION_NAME):
            return

        wiki_collection = mongodb.get_collection(self.WIKI_COLLECTION_NAME)
        wiki_collection.create_index( 
            [("path", ASCENDING)],
            unique=True
        )

    def get_wiki_content(self, title=None):
        if title is None:
            return "Some wiki content"
        # Else get stored wiki content

    def store_wiki_content(self, path, json_content=None):
        mongodb = MongoDb(self.mongodb_connection_string, self.WIKI_DATABASE_NAME)
        wiki_collection = mongodb.get_collection(self.WIKI_COLLECTION_NAME)
        log.info("Get wiki document", path=path)
        document_query = {"path": path}
        wiki_document = wiki_collection.find_one(document_query)
        
        normalized_json_content = {} if json_content is None else json_content
        normalized_json_content['path'] = path

        if wiki_document is None:
            log.debug("insert_one", content=normalized_json_content)
            wiki_record = wiki_collection.insert_one(normalized_json_content)
        else:
            log.debug("replace_one", document_query=document_query, content=normalized_json_content)
            wiki_record = wiki_collection.replace_one(document_query, normalized_json_content, upsert=True)

        return wiki_record
        # Else get stored wiki content
        # mongodb = MongoDb(app_secrets['mongodb:minitools:ConnectionString'], 'minitools')
        # wiki_collection = mongodb.get_collection('wiki')
        # resp = wiki_collection.create_index([ ("field_to_index", ASCENDING) ])
        # wiki_entry = { "title": "CheckEngine", "address": "Highway 37" }
        # wiki_record = wiki_collection.insert_one(wiki_entry)
