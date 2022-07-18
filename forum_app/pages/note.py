from flask import render_template, redirect, url_for
from forum_app import app


@app.route('/note/')
def root_note_page():
    return redirect(url_for('note_dashboard_page'))

@app.route('/note/dashboard')
def note_dashboard_page():
    return render_template('note/note_dashboard.html')

