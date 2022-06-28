# 
################################################################################
# Modules and functions import statements
################################################################################

import logging
import io
from forum_app.modules.barcode import QRCode

from flask import request, abort, send_file

from forum_app import app

@app.route('/api/qr', methods=['GET'])
def api_qr():
    logging.info("In api_qr()")
    query_params = request.args
    if 'd' not in query_params:
        abort(400)
    
    data = query_params['d']
    qrcode = QRCode()
    img = qrcode.make_qr_image(data)

    # data = query_params['d']
    # qr = qrcode.QRCode(version = 1, box_size = 10, border = 5)
    # qr.add_data(data)
    # qr.make(fit = True)
    # img = qr.make_image()
    
    # img = qr.make_image(fill_color = 'red', back_color = 'white')
    img_buf = io.BytesIO()
    img.save(img_buf)
    img_buf.seek(0)
    return send_file(img_buf, mimetype='image/png')

    encoded_img_data = base64.b64encode(data.getvalue())
    img_data = encoded_img_data.decode('utf-8')