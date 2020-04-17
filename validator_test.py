import flask
import pytest

import validator


# Create a fake "app" for generating test request contexts.
@pytest.fixture(scope="module")
def app():
    return flask.Flask(__name__)


def test_get_country_validator(app):
    with app.test_request_context(query_string={"country": "pl"}):
        validator.get_country_validator(flask.request)


def test_get_country_validator_bad_request(app):
    with app.test_request_context():
        with pytest.raises(validator.BadRequest):
            validator.get_country_validator(flask.request)


def test_get_cities_validator(app):
    with app.test_request_context(query_string={"country": "pl"}):
        validator.get_cities_validator(flask.request)


def test_get_cities_validator_bad_request(app):
    with app.test_request_context():
        with pytest.raises(validator.BadRequest):
            validator.get_cities_validator(flask.request)


def test_get_city_validator(app):
    with app.test_request_context(
            query_string={"country": "pl", "city": "krakow"}):
        validator.get_city_validator(flask.request)


@pytest.mark.parametrize("query_string", [
    {"query_string": {}},
    {"query_string": {"country": "pl"}},
    {"query_string": {"city": "krakow"}},
])
def test_get_city_validator_bad_request(app, query_string):
    with app.test_request_context(*query_string):
        with pytest.raises(validator.BadRequest):
            validator.get_city_validator(flask.request)
