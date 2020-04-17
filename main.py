import logging
import os

import flask
import werkzeug
from google.cloud import firestore

import validator
import models

BadRequest = werkzeug.exceptions.BadRequest
NotFound = werkzeug.exceptions.NotFound

db = firestore.Client(
    project=os.getenv("GCP_PROJECT"),
)


def get_countries(_: flask.Request):
    countries_stream = db.collection("countries").stream()
    countries = [
        country.id
        for country in countries_stream
    ]
    return flask.jsonify(countries)


def get_country(request: flask.Request):
    validator.get_country_validator(request)
    country_arg = request.args.get("country")
    logging.info(f"get_country: {country_arg}")
    country_ref = db.document(f"countries/{country_arg}")
    country_doc = country_ref.get()
    if not country_doc.exists:
        raise NotFound
    return flask.jsonify(country_doc.to_dict())


def get_cities(request: flask.Request):
    validator.get_cities_validator(request)
    country_arg = request.args.get("country")
    logging.info(f"get_cities: {country_arg}")
    country_ref = db.document(f"countries/{country_arg}")
    if not country_ref.get().exists:
        raise NotFound
    cities_ref = db.collection("cities")
    query = cities_ref.where("country", "==", country_ref)
    cities = [
        city_doc.id
        for city_doc in query.stream()
    ]
    return flask.jsonify(cities)


def get_city(request: flask.Request):
    validator.get_city_validator(request)
    city_arg = request.args.get("city")
    logging.info(f"get_city: {city_arg}")
    city_ref = db.document(f"cities/{city_arg}")
    city_doc = city_ref.get()
    if not city_doc.exists:
        raise NotFound
    city_years_ref = city_ref.collection("years")
    city_years = [
        models.CityYear.from_dict(city_year_doc.id, city_year_doc.to_dict())
        for city_year_doc in city_years_ref.stream()
    ]
    city = models.City.from_dict(city_doc.to_dict(), city_years)
    return flask.jsonify(city.to_dict())
