from os import path
from flask import make_response
from forum_app import app, app_path
from markdown import markdown
import io

import random
import uuid

from PIL import Image, ImageDraw

@app.route('/art/basic')
def basic_art():
    run_id = uuid.uuid1()

    print(f'Processing run_id: {run_id}')

    image = Image.new('RGB', (2000, 2000))
    width, height = image.size

    rectangle_width = 100
    rectangle_height = 100

    number_of_squares = random.randint(10, 550)

    draw_image = ImageDraw.Draw(image)
    for i in range(number_of_squares):
        rectangle_x = random.randint(0, width)
        rectangle_y = random.randint(0, height)

        rectangle_shape = [
            (rectangle_x, rectangle_y),
            (rectangle_x + rectangle_width, rectangle_y + rectangle_height)]
        draw_image.rectangle(
            rectangle_shape,
            fill=(
                random.randint(0, 255),
                random.randint(0, 255),
                random.randint(0, 255)
            )
        )

    # image.save(f'./output/{run_id}.png')

    img_bytes_buffer = io.BytesIO()
    image.save(img_bytes_buffer, format="png")
    img_bytes_buffer.seek(0)
    # return img_bytes_buffer
    # breakpoint()

    response = make_response(img_bytes_buffer.read())
    response.headers.set('Content-Type', 'image/png')
    # Uncomment to set response as attachment download
    # response.headers.set('Content-Disposition', 'attachment', filename='zc.jpg')
    return response
    

# See also https://github.com/pixegami-team/machine-psychology-python-art/tree/main/src