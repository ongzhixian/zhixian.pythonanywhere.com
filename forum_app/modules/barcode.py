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

    def make_qr_image_bytes(self, data):
        img = self.make_qr_image(data)
        img_bytes_buffer = io.BytesIO()
        img.save(img_bytes_buffer)
        img_bytes_buffer.seek(0)
        return img_bytes_buffer

    def make_qr_image_as_base64(self, data):
        img_bytes_buffer = self.make_qr_image_bytes(data)
        encoded_img_base64 = base64.b64encode(img_bytes_buffer.getvalue())
        return encoded_img_base64.decode('utf-8')
