# Series of pages for MySql administration
from flask import render_template
from forum_app import app

@app.route('/mysql/')
def root_mysql_get():
    """Web page at '/mysql'"""
    #return app.config
    return render_template('mysql/root_mysql_get.html')