from forum_app.features.logging import log
from forum_app.features.mongodb import MongoDb

def __can_connect_to_mongodb(mongodb_connection_string, database_name):
    try:
        MongoDb(mongodb_connection_string, database_name)
        return True
    except Exception:
        log.debug("Cannot connect to MongoDb database", database_name=database_name)
        return False

def __can_access_mongodb_database(app_secrets, database_name):
    
    SECTION_NAME = 'MONGODB'

    if SECTION_NAME not in app_secrets:
        log.debug("Section name not found in secrets.", section_name=SECTION_NAME)
        return False
    
    if database_name not in app_secrets[SECTION_NAME]:
        log.debug("Database name not found in secrets.", section_name=SECTION_NAME, database_name=database_name)
        return False

    connection_string = app_secrets[SECTION_NAME][database_name]

    return __can_connect_to_mongodb('connection_string', database_name)
    

def __can_access_mysql_forum(app_secrets):
    return False


def detect_capabilities(app_path, app_secrets, app_settings):

    log.info("Detecting capabilities...")

    can_access_mongodb_minitools = __can_access_mongodb_database(app_secrets, 'minitools')
    
    can_access_mysql = __can_access_mysql_forum(app_secrets)

    return {
        'can_access_mongodb' : can_access_mongodb_minitools,
        'can_access_mysql' : can_access_mysql
    }