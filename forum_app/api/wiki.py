import json
from flask import render_template, session, request, redirect, url_for
from forum_app import app
from forum_app.features.logging import log
from forum_app.features.wiki import Wiki

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
    OPERATION = "Save wiki document"
    
    if not request.is_json:
        log.info("Bad request")
        return "Bad request", 400

    wiki = Wiki()
    result = wiki.store_wiki_content(request.path, request.json)

    if result is None:
        log.info(OPERATION, status=400, path=request.path, content=request.json)
        return "Bad request", 400
    
    log.debug(OPERATION, status=200, path=request.path, content=request.json)
    
    return "{}"


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


