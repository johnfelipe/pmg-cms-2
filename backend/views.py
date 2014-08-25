from app import db, logger, app, model_dict
import drupal_models as models
import flask
from flask import g, request, abort, redirect, url_for, session, make_response
from functools import wraps
import json
from sqlalchemy import func, or_, distinct
import datetime
from operator import itemgetter
import re
import serializers

API_HOST = app.config["API_HOST"]

# handling static files (only relevant during development)
app.static_folder = 'static'
app.add_url_rule('/static/<path:filename>',
                 endpoint='static',
                 view_func=app.send_static_file)


class ApiException(Exception):
    """
    Class for handling all of our expected API errors.
    """

    def __init__(self, status_code, message):
        Exception.__init__(self)
        self.message = message
        self.status_code = status_code

    def to_dict(self):
        rv = {
            "code": self.status_code,
            "message": self.message
        }
        return rv

@app.errorhandler(ApiException)
def handle_api_exception(error):
    """
    Error handler, used by flask to pass the error on to the user, rather than catching it and throwing a HTTP 500.
    """

    response = flask.jsonify(error.to_dict())
    response.status_code = error.status_code
    response.headers['Access-Control-Allow-Origin'] = "*"
    return response


def send_api_response(data_json):

    response = flask.make_response(data_json)
    response.headers['Access-Control-Allow-Origin'] = "*"
    response.headers['Content-Type'] = "application/json"
    return response


# def login_required(f):
#     @wraps(f)
#     def decorated_function(*args, **kwargs):
#         if g.user is None or not g.user.is_active():
#             raise ApiException(401, "You need to be logged-in in order to access this resource.")
#         return f(*args, **kwargs)
#     return decorated_function
#
#
# @app.before_request
# def load_user():
#
#     user = None
#     # handle authentication via Auth Header
#     if request.headers.get('Authorization') and request.headers['Authorization'].split(":")[0]=="ApiKey":
#         key_value = request.headers['Authorization'].split(":")[1]
#         api_key = ApiKey.query.filter_by(key=key_value).first()
#         if api_key:
#             user = api_key.user
#     # handle authentication via session cookie (for admin)
#     if session and session.get('api_key'):
#         api_key = ApiKey.query.filter_by(key=session.get('api_key')).first()
#         if api_key:
#             user = api_key.user
#     g.user = user
#     return

# -------------------------------------------------------------------
# API endpoints:
#

api_resources = [
    "committee",
    "report",
    "bill",
]

@app.route('/<string:resource>/', )
def resource_list(resource, resource_id=None):
    """
    Generic endpoint for lists of resources.
    """

    if not resource in api_resources:
        raise ApiException(400, "The specified resource type does not exist.")

    model = model_dict[resource]
    count, next = None, None
    # validate paging parameters
    page = 0
    per_page = app.config['RESULTS_PER_PAGE']
    if flask.request.args.get('page'):
        try:
            page = int(flask.request.args.get('page'))
        except ValueError:
            raise ApiException(422, "Please specify a valid 'page'.")
    queryset = db.session.query(model).limit(per_page).offset(page*per_page).all()
    count = db.session.query(func.count('*')).select_from(model).scalar()
    next = None
    if count > (page + 1) * per_page:
        next = flask.request.url_root + resource + "/?page=" + str(page+1)
    out = serializers.queryset_to_json(queryset, count=count, next=next)
    return send_api_response(out)
