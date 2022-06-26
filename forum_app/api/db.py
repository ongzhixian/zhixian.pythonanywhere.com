# 
################################################################################
# Modules and functions import statements
################################################################################

import logging

from forum_app import app
from forum_app.modules.forum_db import ForumDb


@app.route('/api/db/init', methods=['GET', 'POST'])
def api_db_init():
    mydb = ForumDb()
    # mydb.init_new_tables()
    # logging.info("ForumDb initialized.")
    return "All databases initialized."
    