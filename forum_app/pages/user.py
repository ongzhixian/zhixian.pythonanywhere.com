from flask import render_template, session, request, redirect, url_for
from forum_app import app
#from documodules.user import User
from forum_app.modules.user import User

@app.route('/user/')
def root_user_get():
    """Web page at '/user'"""
    return redirect('/user/dashboard')

@app.route('/user/dashboard')
def user_dashboard_page():
    """Web page at '/user/dashboard'"""
    user = User()
    users = user.get_users()
    return render_template('user/user_dashboard.html', users=users)
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

@app.route('/user/add')
def user_add_page():
    """Web page at '/user/add'"""
    return render_template('user/user_add.html')

@app.route('/user/add', methods=['POST'])
def user_add_post():
    """Web page at '/user/add'"""
    import pdb
    # query_params = request.args
    # if 'd' in query_params:
    #     data = query_params['d']

    username = request.form['username'] if 'username' in request.form else ''
    password = request.form['password'] if 'password' in request.form else ''
    print(username)
    print(password)
    user = User()
    user.add(username, password)

    return render_template('user/user_add.html')