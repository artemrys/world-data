import os

import flask
import werkzeug
from google.cloud import firestore

import validator

BadRequest = werkzeug.exceptions.BadRequest
NotFound = werkzeug.exceptions.NotFound

db = firestore.Client(
    project=os.getenv("GCP_PROJECT"),
)


def get_countries(_: flask.Request):
    docs = db.collection("countries").stream()
    countries = [
        doc.id
        for doc in docs
    ]
    return flask.jsonify({"countries": countries})


def get_country(request: flask.Request):
    validator.get_country_validator(request)
    country = request.args.get("country")
    doc_ref = db.document(f"countries/{country}")
    doc = doc_ref.get()
    if not doc.exists:
        raise NotFound
    return flask.jsonify({"country": doc.to_dict()})


def get_cities(request: flask.Request):
    validator.get_cities_validator(request)
    country = request.args.get("country")
    country_ref = db.document(f"countries/{country}")
    country_doc = country_ref.get()
    if not country_doc.exists:
        raise NotFound
    cities = [
        city.id
        for city in db.collection(f"countries/{country}/cities").stream()
    ]
    return flask.jsonify({"cities": cities})


def get_city(request: flask.Request):
    validator.get_city_validator(request)
    country = request.args.get("country")
    city = request.args.get("city")
    doc_ref = db.document(f"countries/{country}/cities/{city}")
    doc = doc_ref.get()
    if not doc.exists:
        raise NotFound
    return flask.jsonify({"city": doc.to_dict()})
