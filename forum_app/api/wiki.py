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
        log.info(OPERATION, operation=api_wiki_default_post.__name__, status=400, status_text="Bad request", status_description="Request is not JSON", )
        return "Bad request", 400

    json_data = request.json
    wiki_path = json_data['path'] if 'path' in json_data else None

    log.debug(OPERATION, operation=api_wiki_default_post.__name__, content=json_data)

    wiki = Wiki()
    result = wiki.store_wiki_content(wiki_path, request.json)

    if result is None:
        log.info(OPERATION, operation=api_wiki_default_post.__name__, status=400, status_text="Bad request", status_description="Result is None", )
        return "Bad request", 400
    
    log.debug(OPERATION, status=200, path=request.path)
    
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


