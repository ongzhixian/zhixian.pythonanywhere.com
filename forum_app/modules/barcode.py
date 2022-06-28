import logging as log
import io
import qrcode
import base64

class QRCode:
    def __init__(self):
        pass
        # log.info(f"Init {connection_string}")
    
    def make_qr_image(self, data):
        qr = qrcode.QRCode(version = 1, box_size = 10, border = 5)
        qr.add_data(data)
        qr.make(fit = True)
        return qr.make_image()

    def make_qr_image_as_base64(self, data):
        qr = qrcode.QRCode(version = 1, box_size = 10, border = 5)
        qr.add_data(data)
        qr.make(fit = True)
        img = qr.make_image()

        img_buf = io.BytesIO()
        img.save(img_buf)
        img_buf.seek(0)

        encoded_img_data = base64.b64encode(img_buf.getvalue())
        img_data = encoded_img_data.decode('utf-8')
        return img_data
        