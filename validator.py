import flask
import werkzeug

BadRequest = werkzeug.exceptions.BadRequest


def get_country_validator(request: flask.Request):
    if request.args.get("country") is None:
        raise BadRequest


def get_cities_validator(request: flask.Request):
    if request.args.get("country") is None:
        raise BadRequest


def get_city_validator(request: flask.Request):
    if request.args.get("city") is None:
        raise BadRequest
