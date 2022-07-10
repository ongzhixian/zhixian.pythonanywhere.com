from flask import render_template, session, request, redirect, url_for
from forum_app import app

@app.route('/shared-data/')
def root_shared_data_get():
    """Web page at '/shared-data'"""
    return redirect('/shared-data/dashboard')

@app.route('/shared-data/dashboard')
def shared_data_dashboard_page():
    """Web page at '/shared-data/dashboard'"""
    to_implement_data_list = [
        "Country codes", 
        "Market Identifier Code (MIC) (ISO 10383)",
        
        "Classification of Financial Instruments (CFI) (ISO 10962)",
        
        "International Securities Identification Number (ISIN) (ISO 6166)",
        "Committee on Uniform Securities Identification Procedures (CUSIP) number"
        "Stock Exchange Daily Official List (SEDOL)",
        "Bloomberg ticker",
        "Reuters Instrument code ticker",
        "Yahoo ticker",

        "Wertpapierkennnummer",
        "IATA ICAO",

        "Society for Worldwide Interbank Financial Telecommunication (SWIFT)",
        "Business Identifier Codes (BIC) (ISO 9362)"
        "International Bank Account Number (IBAN)",
        "Legal Entity Identifier (LEI) (ISO 17442)",
        "Data Universal Numbering System (DUNS)",

        
    ]
    return render_template('shared_data/shared_data_dashboard.html', users=[], to_implement_data_list=to_implement_data_list)
    