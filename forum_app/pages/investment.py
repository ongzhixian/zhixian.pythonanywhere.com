from flask import render_template, redirect, url_for
from forum_app import app


@app.route('/investment/')
def investment_trade_get():
    """Web page at '/investment'"""
    return redirect(url_for('investment_dashboard_page'))

@app.route('/investment/dashboard')
def investment_dashboard_page():
    """Web page at '/investment/dashboard'"""
    return render_template('investment/investment_dashboard.html')
