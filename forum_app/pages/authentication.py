from flask import render_template, session, request, redirect, url_for
from flask.sessions import NullSession

from forum_app import app
from forum_app.features import is_feature_enable
from forum_app.features.login import LoginFeature

@app.route('/login', methods=['GET', 'POST'])
def login():
    if not is_feature_enable('Authentication'):
        return redirect('/')

    message = None
    if request.method == 'POST':
        username = request.form.get("username_field")
        password = request.form.get("password_field")
        login = LoginFeature()
        if login.is_valid_credential(username, password):
            session['username'] = username
            return redirect('/')
        message = "Invalid credentials."

    return render_template('authentication/login_get.html', message = message)

@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    if session != NullSession():
        session.pop('username', None)
    return redirect(url_for('login'))
