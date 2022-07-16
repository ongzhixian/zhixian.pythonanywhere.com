import logging
from flask import g, render_template, request, session, redirect
from forum_app import app
from forum_app.helpers.auth import login_required
from forum_app.modules.barcode import QRCode
from forum_app.features.authentication import authentication_check

@app.route('/')
@authentication_check
def root_get():
    """GET /"""
    return render_template('root_get.html')

@app.route('/forum')
@login_required
def forum_get():
    """TODO: Reorganize; GET /"""
    
    return render_template('forum_get.html')

@app.route('/chart-examples')
@login_required
def chart_examples_get():
    """TODO: Reorganize; GET /"""
    return render_template('chart_examples_get.html')

@app.route('/qrcode')
def qrcode_get():
    """TODO: Reorganize; GET /"""
    data = "dummy qr data"
    
    query_params = request.args

    if 'd' in query_params:
        data = query_params['d']
        
    qrcode = QRCode()
    qr_img_base64 = qrcode.make_qr_image_as_base64(data)
    
    return render_template('qrcode_get.html', model = {
        "qr_img_base64" : qr_img_base64
    })

@app.route('/link-dump', methods=['GET', 'POST'])
@login_required
def link_dump_get():
    """TODO: Reorganize; GET /"""
    # if request.method == 'POST':
    #     url_text = request.form['urlText']
    #     url_list = url_text.splitlines()
    #     data = []
    #     if len(url_list) > 0:
    #         for url in url_list:
    #             data.append((url, ))
    #         mydb = ForumDb()
    #         mydb.add_weblinks(data)
    
    return render_template('link_dump_get.html')