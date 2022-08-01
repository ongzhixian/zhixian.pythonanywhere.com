from flask import render_template, session, request, redirect, url_for
from forum_app import app
from forum_app.modules.zzz_user import User

@app.route('/user/')
def root_user_get():
    """Web page at '/user'"""
    return redirect('/user/dashboard')

@app.route('/user/dashboard')
def user_dashboard_page():
    """Web page at '/user/dashboard'"""
    user = User()
    user_login_list = user.get_user_logins()
    return render_template('user/user_dashboard.html', user_login=user_login_list)


@app.route('/user/add')
def user_add_page():
    """Web page at '/user/add'"""
    return render_template('user/user_add.html')


def validate_form_input(username, password):
    """Validate form input"""
    if username is None or username.strip() == '' or password is None or password.strip() == '':
        return (False, "Username and password are required")
    return (True, None)

@app.route('/user/add', methods=['POST'])
def user_add_post():
    """Web page at '/user/add'"""
    username = request.form['username_field'] if 'username_field' in request.form else ''
    password = request.form['password_field'] if 'password_field' in request.form else ''

    (is_valid_form_input, error_message) = validate_form_input(username, password)
    if not is_valid_form_input:
        return render_template('user/user_add.html', message={
            'type': 'error',
            'text': error_message
        })

    user = User()
    (rows_affected, error_message) = user.add(username, password)

    if rows_affected <= 0:
        return render_template('user/user_add.html', message={
            'type': 'error',
            'text': error_message
        })

    return render_template('user/user_add.html', message={
        'type': 'success',
        'text': f"User {username} added"
    })



@app.route('/user/profile')
def user_profile_page():
    """Web page at '/user/profile'"""
    return render_template('user/user_profile.html')


def update_user_profile(form):
    pass
    first_name_field = form['first_name_field']
    last_name_field = form['last_name_field']
    email_field = form['email_field']
    from forum_app.features.user_profile import UserProfileFeature
    user_profile = UserProfileFeature()
    user_profile.update_profile(
        first_name_field, 
        last_name_field,
        email_field
    )
    breakpoint()

@app.route('/user/profile', methods=['POST'])
def user_profile_post():
    """Web page at '/user/profile'"""
    # update-user-profile
    # update-user-password
    # update-profile-picture
    # update-background-picture
    actions = {
        'update-user-profile': update_user_profile,
        'update-user-password': update_user_profile,
        'update-profile-picture': update_user_profile,
        'update-background-picture': update_user_profile,
    }
    if 'action' not in request.form:
        return render_template('user/user_profile.html')

    action = request.form['action']
    if action in actions:
        actions[action](request.form)
    return render_template('user/user_profile.html')


@app.route('/user/password-test')
def user_password_test_page():
    """Web page at '/user/password-test'"""
    return render_template('user/user_password_test.html')