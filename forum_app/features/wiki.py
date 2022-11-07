from pymongo import ASCENDING
from forum_app.features.mongodb import MongoDb

WIKI_DATABASE_NAME = 'minitools'
WIKI_COLLECTION_NAME = 'wiki'

def init_wiki_collection(mongodb):
    if not mongodb.collection_exists(WIKI_COLLECTION_NAME):
        wiki_collection = mongodb.get_collection(WIKI_COLLECTION_NAME)
        wiki_collection.create_index( 
            [("title", ASCENDING)],
            unique=True
        )

def init_wiki(mongodb_connection_string):
    mongodb = MongoDb(mongodb_connection_string, WIKI_DATABASE_NAME)
    init_wiki_collection(mongodb)


def get_wiki_content(title=None):
    if title is None:
        return "Some wiki content"
    # Else get stored wiki content


def store_wiki_content(title=None, content=None):
    if title is None:
        return "Some wiki content"

    # Else get stored wiki content
    # mongodb = MongoDb(app_secrets['mongodb:minitools:ConnectionString'], 'minitools')
    # wiki_collection = mongodb.get_collection('wiki')
    # resp = wiki_collection.create_index([ ("field_to_index", ASCENDING) ])
    # wiki_entry = { "title": "CheckEngine", "address": "Highway 37" }
    # wiki_record = wiki_collection.insert_one(wiki_entry)


