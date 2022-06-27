# Series of pages for MySql administration

import os
import logging
from flask import redirect, render_template
from forum_app import app
from forum_app.modules.forum_db import ForumDb
from mysql.connector.errors import ProgrammingError

from flask import render_template, session, request, redirect, url_for

@app.route('/database/')
def root_database_get():
    """Web page at '/database'"""
    # Need a rethink on navigation; for now redirect to dashboard
    # return render_template('database/root_database_get.html')
    return redirect('/database/dashboard')

@app.route('/database/init')
def database_initialization():
    """Web page at '/database/dashboard'"""
    initialize_database()
    return redirect('/database/dashboard')

@app.route('/database/dashboard')
def database_dashboard_page():
    """Web page at '/database/dashboard'"""
    # try:
    discover_database_scripts()

    unapplied_db_migrate_count = get_unapplied_db_migrate_count()

    (table_count, view_count, procedure_count, function_count) = get_schema_object_count()

    return render_template('database/database_dashboard.html', model = {
        'unapplied_db_migrate_count' : unapplied_db_migrate_count,
        'table_count' : table_count,
        'view_count' : view_count,
        'procedure_count' : procedure_count,
        'function_count' : function_count
    })
    # except ProgrammingError as e:
    #     if e.errno == 1146: # 1146 is MySql specific error code for 'no such table'
    #         pass
    #         initialize_database()
    #         # Create table and any
    

@app.route('/database/update')
def database_update_page():
    """Web page at '/database/update'"""
    
    update_list = get_unapplied_db_migrate_list()

    return render_template('database/database_update.html', model={
        'updates': update_list
    })
    

@app.route('/database/apply-update', methods=['POST'])
def database_apply_update_handler():
    import pdb
    # POC EXAMPLE
    logging.info("database_apply_update_handler")
    if request.method == 'POST':
        # session['username'] = username
        action = request.form.get("action")
        updateIdList = request.form.get("updateIdList")
        if action == 'apply-update':
            pass

    return redirect('/database/update')

@app.route('/database/help')
def database_help_get():
    """Web page at '/database/help'"""
    #return app.config
    return render_template('database/database_help_get.html')


def discover_database_scripts():

    DB_SCRIPTS_PATH = os.path.join(os.getcwd(), 'forum_app', 'data', 'database_scripts')

    logging.info(f"Discovering database scripts in {DB_SCRIPTS_PATH}")

    mydb = ForumDb()

    for dirpath, _, files in os.walk(DB_SCRIPTS_PATH):
        for file_name in files:
            file_relative_path = os.path.relpath(os.path.join(dirpath, file_name), DB_SCRIPTS_PATH)
            # For each file_relative_path, insert it into _db_migrate table (if it does not exists)
            #print(os.path.join(dirpath, file_name))
            logging.info(f"Found file_relative_path [{file_relative_path}]")
            if not mydb.db_migrate_exists(file_relative_path):
                mydb.add_db_migrate(file_relative_path)

def get_unapplied_db_migrate_count():
    mydb = ForumDb()
    return mydb.get_unapplied_db_migrate_count()

def get_unapplied_db_migrate_list():
    mydb = ForumDb()
    return mydb.get_unapplied_db_migrate_list()

def get_schema_object_count():
    mydb = ForumDb()
    return mydb.get_schema_object_count()

def initialize_database():
    mydb = ForumDb()
    mydb.one_time_initialization()