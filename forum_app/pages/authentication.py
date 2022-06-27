from flask import render_template, session, request, redirect, url_for
from forum_app import app

# @app.route('/login')
# def login_get():
#     """GET /login"""
#     #return app.config
#     return render_template('authentication/login_get.html')


# @app.route('/login', methods=['POST'])
# def login_post():
#     """POST /login"""
#     return "sad"    


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # import pdb
        # pdb.set_trace()
        username = request.form.get("username_field")
        password = request.form.get("password_field")
        session['username'] = username
        return redirect('/')
        #return redirect(url_for('/'))
        #session['username'] = request.form['username_field']
        #return redirect(url_for('index'))

    return render_template('authentication/login_get.html')

@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    return redirect(url_for('login'))