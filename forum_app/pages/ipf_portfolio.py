from flask import render_template, redirect, url_for
from forum_app import app

# from forum_app.features.wms import WmsFeature
# from forum_app.features.wms_location import WmsLocationFeature
# from forum_app.features.wms_location_type import WmsLocationTypeFeature
from forum_app.features.ipf_portfolio import IpfPortfolioFeature

@app.route('/ipf/portfolio/')
def ipf_portfolio_get():
    """/ipf/portfolio"""
    # return render_template('wms/wms_location_type_list.html')
    return redirect(url_for('wms_location_type_list'))

@app.route('/ipf/portfolio/list')
def ipf_portfolio_list():
    """Url: /ipf/portfolio/list
    """
    breadcrumbs = [
        { 'href' : '/ipf/dashboard', 'text': 'IPF' },
        { 'href' : None, 'text': 'IPF Portfolio' }
    ]
    # wms = WmsFeature()
    # wms_location = WmsLocationFeature()
    # wms_location_type = WmsLocationTypeFeature()
    # location_list = wms_location.get_location_list()
    # wms_location_type_list = wms_location_type.get_location_type_list()
    
    # dashboard_list = wms.get_dashboard_list()
    ipf_portfolio = IpfPortfolioFeature()
    portfolio_list = ipf_portfolio.list()
    
    return render_template(
        'ipf/ipf_portfolio_list.html',
        breadcrumbs=breadcrumbs,
        portfolio_list=portfolio_list)


@app.route('/ipf/portfolio/<id>')
def ipf_portfolio_id(id):
    """Url: /ipf/portfolio/<id>
    """
    breadcrumbs = [
        { 'href' : '/ipf/dashboard', 'text': 'IPF' },
        { 'href' : None, 'text': 'IPF Portfolio' }
    ]

    # dashboard_list = wms.get_dashboard_list()
    ipf_portfolio = IpfPortfolioFeature()
    portfolio_list = ipf_portfolio.list()
    
    return render_template(
        'ipf/ipf_portfolio_detail.html',
        breadcrumbs=breadcrumbs,
        portfolio_list=portfolio_list)
