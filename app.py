from flask import Flask, request

import main

app = Flask(__name__)


@app.route("/api/v1/countries", methods=["GET"])
def countries():
    return main.get_countries(request)


@app.route("/api/v1/country", methods=["GET"])
def country():
    return main.get_country(request)


@app.route("/api/v1/cities", methods=["GET"])
def cities():
    return main.get_cities(request)


@app.route("/api/v1/city", methods=["GET"])
def city():
    return main.get_city(request)


if __name__ == '__main__':
    app.run(debug=True)
