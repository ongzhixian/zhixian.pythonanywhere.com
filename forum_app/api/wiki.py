import logging
from forum_app import app

@app.route('/api/wiki/', methods=['GET'])
def api_wiki_default_get(title):
    result = None

    if result is None:
        return "Bad request", 400
    else:
        return str(result)


@app.route('/api/wiki/', methods=['POST'])
def api_wiki_default_post():
    """"""
    logging.info("Save default wiki page")
    print("Save default wiki page")

    result = None

    if result is None:
        return "Bad request", 400
    else:
        return str(result)


@app.route('/api/wiki/<string:title>', methods=['GET'])
def api_wiki_get(title):
    result = None

    if result is None:
        return "Bad request", 400
    else:
        return str(result)

@app.route('/api/wiki/<string:title>', methods=['POST'])
def api_wiki_post(title):
    result = None

    if result is None:
        return "Bad request", 400
    else:
        return str(result)


