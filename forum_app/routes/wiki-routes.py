
from flask import g, render_template, request, session, redirect
from markupsafe import escape
from forum_app import app
from forum_app.features.logging import log
from markdown import markdown

# from forum_app.helpers.auth import login_required
# from forum_app.modules.barcode import QRCode
# from forum_app.features.authentication import authentication_check

from forum_app.features.wiki import Wiki

DEFAULT_WIKI_PATH = '/wiki/'

@app.route("/code-review/")
def code_review_root_page_get():
    return render_template('root.jinja')

@app.route("/wiki/")
def wiki_default_page_get():
    wiki = Wiki()
    wiki_content = wiki.get_wiki_content(DEFAULT_WIKI_PATH)
    wiki_content = wiki_content.replace('\xa0', ' ')
    html = markdown(wiki_content)
    return render_template('wiki.jinja', wiki_content=html, wiki_title="", wiki_path=DEFAULT_WIKI_PATH)


@app.route("/wiki/<string:title>")
def wiki_page_get(title):
    wiki_path = f'/wiki/{title}'
    wiki = Wiki()
    wiki_content = wiki.get_wiki_content(wiki_path)
    wiki_content = wiki_content.replace('\xa0', ' ')
    import re
    res = re.findall("(\[\[(.+)\]\])", wiki_content)
    for link in res:
        wiki_content = wiki_content.replace(link[0], f'<a href="/wiki/{link[1]}">{link[1]}</a>')
    
    html = markdown(wiki_content)
    return render_template('wiki.jinja', wiki_content=html, wiki_title=title, wiki_path=wiki_path)


@app.route("/wiki-editor/")
def wiki_editor_default_page_get():
    wiki = Wiki()
    wiki_content = wiki.get_wiki_editor_content(DEFAULT_WIKI_PATH)
    return render_template('wiki-editor.jinja', wiki_content=wiki_content, wiki_title="", wiki_path=DEFAULT_WIKI_PATH)


@app.route("/wiki-editor/<string:title>")
def wiki_editor_page_get(title):
    wiki_path = f'/wiki/{title}'
    wiki = Wiki()
    wiki_content = wiki.get_wiki_editor_content(wiki_path)
    return render_template('wiki-editor.jinja', wiki_content=wiki_content, wiki_title=title, wiki_path=wiki_path)


# @app.route('/favicon.ico')
# # @authentication_check
# def favicon_ico_get():
#     """Path: /favicon.ico"""
#     # logging.debug(f"Username: {g.username}")
#     # return render_template('root_get.html')
#     return "", 201
