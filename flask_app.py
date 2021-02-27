import logging
import os

from forum_app import app

if __name__ == '__main__':
    logging.info(str(os.environ))
    app.run(host='0.0.0.0', port=31000, debug=True)