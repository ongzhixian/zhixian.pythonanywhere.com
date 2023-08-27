import json
# from flask import render_template, session, request, redirect, url_for
from forum_app import app
from apispec import APISpec

from flask import Response

@app.route('/api/swagger', methods=['GET'])
def api_swagger_json():
    # Read before use: http://flask.pocoo.org/docs/0.12/api/#flask.send_file
    # return send_file('path/to/swagger.json')
    # spec = swagger_api_spec()
    # to_dict() returns as JSON; use to_yaml() to return YAML
    return swagger_api_spec().to_dict(), 200, { 'Content-Type': 'application/json; charset=utf-8' }
    

# @app.route('/api/wiki/', methods=['GET'])
# def api_wiki_default_get(title):
#     result = None
#     if result is None:
#         return "Bad request", 400
#     else:
#         return str(result)


def swagger_api_spec():
    spec = APISpec(
        title="Gisty",
        version="1.0.0",
        openapi_version="3.0.2",
        info=dict(description="A minimal gist API"),
    )

    spec.components.schema(
        "Gist",
        {
            "properties": {
                "id": {"type": "integer", "format": "int64"},
                "name": {"type": "string"},
            }
        },
    )

    spec.path(
        path="/gist/{gist_id}",
        operations=dict(
            get=dict(
                responses={"200": {"content": {"application/json": {"schema": "Gist"}}}}
            )
        ),
    )

    return spec