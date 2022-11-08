from pymongo import ASCENDING
from forum_app.features.logging import log
from forum_app.features.mongodb import MongoDb

class Wiki(object):
    WIKI_DATABASE_NAME = 'minitools'
    WIKI_COLLECTION_NAME = 'wiki'

    def __new__(cls, *args):
        if hasattr(cls, 'instance'):
            log.debug("Reuse wiki instance")
            return cls.instance

        log.debug("Create wiki instance")
        cls.instance = super(Wiki, cls).__new__(cls)
        return cls.instance

    def __init__(self, mongodb_connection_string=None):
        if mongodb_connection_string is not None:
            log.debug("Initialize wiki")
            self.mongodb_connection_string = mongodb_connection_string
            mongodb = MongoDb(self.mongodb_connection_string, self.WIKI_DATABASE_NAME)
            self.init_wiki_collection(mongodb)

    def init_wiki_collection(self, mongodb):
        if mongodb.collection_exists(self.WIKI_COLLECTION_NAME):
            return

        wiki_collection = mongodb.get_collection(self.WIKI_COLLECTION_NAME)
        wiki_collection.create_index( 
            [("path", ASCENDING)],
            unique=True
        )


    def get_wiki_content(self, path=None):
        wiki_document = self.get_wiki_document(path)
        return "" if wiki_document is None else wiki_document['content']

    def get_wiki_editor_content(self, path=None):
        wiki_document = self.get_wiki_document(path)
        return "" if wiki_document is None else wiki_document['editorContent']


    def get_wiki_document(self, wiki_path=None):
        if wiki_path is None:
            return None
        
        document_query = {"path": wiki_path}
        mongodb = MongoDb(self.mongodb_connection_string, self.WIKI_DATABASE_NAME)
        wiki_collection = mongodb.get_collection(self.WIKI_COLLECTION_NAME)
        wiki_document = wiki_collection.find_one(document_query)

        log.info("Get wiki document", path=wiki_path)
        return wiki_document


    def store_wiki_content(self, wiki_path, json_content=None):
        if wiki_path is None:
            return None

        mongodb = MongoDb(self.mongodb_connection_string, self.WIKI_DATABASE_NAME)
        wiki_collection = mongodb.get_collection(self.WIKI_COLLECTION_NAME)
        wiki_document = self.get_wiki_document(wiki_path)
        
        normalized_json_content = {} if json_content is None else json_content
        # normalized_json_content['path'] = path

        if wiki_document is None:
            log.debug("insert_one", wiki_path=wiki_path, content=normalized_json_content)
            wiki_record = wiki_collection.insert_one(normalized_json_content)
        else:
            log.debug("replace_one", wiki_path=wiki_path, content=normalized_json_content)
            wiki_record = wiki_collection.replace_one({"path": wiki_path}, normalized_json_content, upsert=True)
        return wiki_record
        # Else get stored wiki content
        # mongodb = MongoDb(app_secrets['mongodb:minitools:ConnectionString'], 'minitools')
        # wiki_collection = mongodb.get_collection('wiki')
        # resp = wiki_collection.create_index([ ("field_to_index", ASCENDING) ])
        # wiki_entry = { "title": "CheckEngine", "address": "Highway 37" }
        # wiki_record = wiki_collection.insert_one(wiki_entry)
