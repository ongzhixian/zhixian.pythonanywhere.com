import logging
from flask import render_template, session, request, redirect, url_for
from forum_app import app, app_path
from os import abort, path


@app.route('/trade/')
def root_trade_get():
    """Web page at '/trade'"""
    return redirect('/trade/dashboard')

@app.route('/trade/dashboard')
def trade_dashboard_page():
    """Web page at '/trade/dashboard'"""
    # portfolio = PortfolioFeature()
    # records = portfolio.get_portfolio_list()
    return render_template('trade/trade_dashboard.html')



@app.route('/trade/oanda')
def trade_oanda_page():
    """Web page at '/trade/trading-api-list'"""
    return render_template('trade/trade_oanda.html')


@app.route('/trade/trading-api-list')
def trade_trading_api_list_page():
    """Web page at '/trade/trading-api-list'"""
    return render_template('trade/trade_trading_api_list.html')


@app.route('/trade/add-trading-api')
def trade_add_trading_api_page():
    """Web page at '/trade/trading-api-list'"""
    return render_template('trade/add_trading_api.html')

@app.route('/trade/add-trading-api', methods=['POST'])
def trade_add_trading_api_post():
    """Web page at '/trade/trading-api-list'"""
    token_type = request.form['token_type']
    token_name = request.form['token_name']
    token_value = request.form['token_value']
    logging.debug(f"{token_type}, {token_name}, {token_value}")
    
    return render_template('trade/add_trading_api.html')


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