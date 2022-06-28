import logging
from flask import render_template, request, session, redirect
from forum_app import app
from forum_app.helpers.auth import login_required
from forum_app.modules.barcode import QRCode
from forum_app.modules.forum_db import ForumDb

@app.route('/')
@login_required
def root_get():
    """GET /"""
    return render_template('root_get.html')

@app.route('/forum')
@login_required
def forum_get():
    """GET /"""
    return render_template('forum_get.html')

@app.route('/chart-examples')
@login_required
def chart_examples_get():
    """GET /"""
    return render_template('chart_examples_get.html')

@app.route('/qrcode')
def qrcode_get():
    """GET /"""
    # import pdb
    # query_params = request.args
    # if 'd' in query_params:
    #     pass
    #     import qrcode
    #     data = query_params['d']
    #     qr = qrcode.QRCode(version = 1, box_size = 10, border = 5)
    #     qr.add_data(data)
    #     qr.make(fit = True)
    #     # img = qr.make_image(fill_color = 'red', back_color = 'white')
    #     img = qr.make_image()
    #     img.save('MyQRCode2.png')
    #     pdb.set_trace()
    data = "some qr code"
    qrcode = QRCode()
    qr_img_base64 = qrcode.make_qr_image_as_base64(data)
    
    return render_template('qrcode_get.html', model = {
        "qr_img_base64" : qr_img_base64
    })

@app.route('/link-dump', methods=['GET', 'POST'])
@login_required
def link_dump_get():
    """GET /"""
    if request.method == 'POST':
        url_text = request.form['urlText']
        url_list = url_text.splitlines()
        data = []
        if len(url_list) > 0:
            for url in url_list:
                data.append((url, ))
            mydb = ForumDb()
            mydb.add_weblinks(data)
    
    return render_template('link_dump_get.html')