import logging
from flask import render_template, session, request, redirect, url_for
from forum_app import app, app_path
from os import abort, path

from forum_app.features.investment_portfolio import InvestmentPortfolioFeature


@app.route('/investment/')
def investment_trade_get():
    """Web page at '/investment'"""
    # portfolio = PortfolioFeature()
    # records = portfolio.get_portfolio_list()
    # return redirect('/portfolio/dashboard', portfolio_list=records)
    return redirect('/investment/dashboard')

@app.route('/investment/dashboard')
def investment_dashboard_page():
    """Web page at '/investment/dashboard'"""
    # portfolio = PortfolioFeature()
    # records = portfolio.get_portfolio_list()
    return render_template('investment/investment_dashboard.html')


# @app.route('/portfolio/detail/<portfolio_id>')
# def portfolio_detail_page(portfolio_id):
#     """Web page at '/portfolio/<portfolio_id>'"""
#     position_list = []
#     return render_template('/portfolio/portfolio_detail.html',
#         position_list=position_list)



# @app.route('/portfolio/new')
# def portfolio_new_page():
#     """Web page at '/client/new'"""
#     # Get a list of client types
#     # SELECT id, name FROM client_type ORDER BY name;
    
#     client = PortfolioFeature()
#     client_type_list = client.get_client_type_list()
#     selected_client_type = 1
#     return render_template('client/new_client.html', 
#         selected_client_type=selected_client_type,
#         client_type_list=client_type_list)

# @app.route('/portfolio/new', methods=['POST'])
# def portfolio_new_post():
#     """Web page at '/client/new'"""
#     client_name_field = request.form.get("client_name_field")
#     client_type_dropdown = request.form.get("client_type_dropdown")

#     client = PortfolioFeature()
#     rows_affected = client.add_new(client_name_field, client_type_dropdown)
#     client_type_list = client.get_client_type_list()
#     message = 'Success' if rows_affected > 0 else 'Failed'
#     return render_template('client/new_client.html', 
#         selected_client_type=client_type_dropdown,
#         client_type_list=client_type_list,
#         message=message)