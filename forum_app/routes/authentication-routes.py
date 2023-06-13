from flask import g, render_template, request, session, redirect, url_for
from markupsafe import escape
from forum_app import app
from forum_app.features.logging import log
from markdown import markdown

def is_valid_credentials(username, password):
    return True

@app.route('/login')
# @authentication_check
def login():
    return render_template('login.html', model=None)

@app.route('/login', methods=['POST'])
# @authentication_check
def login_post():
    form = request.form
    if 'username' in form and 'password' in form:
        username = form['username']
        password = form['password']
        if is_valid_credentials(username, password):
            session['username'] = username
            return redirect(url_for("home"))
    return render_template('login.html', model={
        'message': "Invalid credentials"
    })


@app.route('/logout')
def logout():
    session.pop('username')
    return redirect("login")
    # return render_template('login.html', model=None)