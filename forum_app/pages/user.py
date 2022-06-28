from flask import render_template, session, request, redirect, url_for
from forum_app import app

@app.route('/user/')
def root_user_get():
    """Web page at '/user'"""
    return redirect('/user/dashboard')

@app.route('/user/dashboard')
def user_dashboard_page():
    """Web page at '/user/dashboard'"""
    return render_template('user/user_dashboard.html')
    # return render_template('database/database_dashboard.html', model = {
    #     'unapplied_db_migrate_count' : unapplied_db_migrate_count,
    #     'table_count' : table_count,
    #     'view_count' : view_count,
    #     'procedure_count' : procedure_count,
    #     'function_count' : function_count
    # })
    # except ProgrammingError as e:
    #     if e.errno == 1146: # 1146 is MySql specific error code for 'no such table'
    #         pass
    #         initialize_database()
    #         # Create table and any
