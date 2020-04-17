import os

import requests

ENDPOINTS_HOST = os.getenv("ENDPOINTS_HOST")
ENDPOINTS_KEY = os.getenv("ENDPOINTS_KEY")


def test_get_countries():
    payload = {"key": ENDPOINTS_KEY}
    resp = requests.get(f"{ENDPOINTS_HOST}/api/v1/countries", params=payload)
    assert resp.status_code == 200


def test_get_country():
    payload = {"key": ENDPOINTS_KEY}
    resp = requests.get(f"{ENDPOINTS_HOST}/api/v1/countries/pl", params=payload)
    assert resp.status_code == 200


def test_get_country_when_no_such_country():
    payload = {"key": ENDPOINTS_KEY}
    resp = requests.get(
        f"{ENDPOINTS_HOST}/api/v1/countries/nosuchcountry", params=payload)
    assert resp.status_code == 404


def test_get_cities():
    payload = {"key": ENDPOINTS_KEY}
    resp = requests.get(
        f"{ENDPOINTS_HOST}/api/v1/countries/pl/cities", params=payload)
    assert resp.status_code == 200


def test_get_cities_when_no_such_country():
    payload = {"key": ENDPOINTS_KEY}
    resp = requests.get(
        f"{ENDPOINTS_HOST}/api/v1/countries/nosuchcountry/cities",
        params=payload)
    assert resp.status_code == 404


def test_get_city():
    payload = {"key": ENDPOINTS_KEY}
    resp = requests.get(
        f"{ENDPOINTS_HOST}/api/v1/cities/cracow",
        params=payload)
    assert resp.status_code == 200


def test_get_city_when_no_such_city():
    payload = {"key": ENDPOINTS_KEY}
    resp = requests.get(
        f"{ENDPOINTS_HOST}/api/v1/cities/nosuchcity",
        params=payload)
    assert resp.status_code == 404
