from flask import render_template, session, request, redirect, url_for
from forum_app import app
from forum_app.modules.role import Role

@app.route('/role/')
def root_role_get():
    """Web page at '/role'"""
    return redirect('/role/dashboard')

@app.route('/role/dashboard')
def role_dashboard_page():
    """Web page at '/role/dashboard'"""
    role = Role()
    role_list = role.get_roles()
    return render_template('role/role_dashboard.html', record_list=role_list)

