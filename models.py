from typing import Dict, List, Optional

from google.cloud import firestore


class CityYear(object):
    def __init__(self,
                 year: int,
                 population: int):
        self.year = year
        self.population = population

    @classmethod
    def from_dict(cls,
                  year: int,
                  source: Dict):
        return CityYear(
            year,
            source["population"])

    def to_dict(self):
        return {
            "year": self.year,
            "population": self.population,
        }

    def __repr__(self):
        return f"<CityYear population={self.population}>"


class City(object):
    def __init__(self,
                 name: str,
                 coordinates: firestore.GeoPoint,
                 country_ref: firestore.DocumentReference,
                 years_info: Optional[List[CityYear]] = None):
        self.name = name
        self.coordinates = coordinates
        self.years_info = years_info
        self.country_ref = country_ref

    @classmethod
    def from_dict(cls,
                  source: Dict,
                  years_info: Optional[List[CityYear]] = None):
        return City(
            source["name"],
            source["coordinates"],
            source["country"],
            years_info)

    def to_dict(self):
        return {
            "name": self.name,
            "latitude": self.coordinates.latitude,
            "longitude": self.coordinates.longitude,
            "years": [
                year_info.to_dict()
                for year_info in self.years_info
            ]
        }

    def __repr__(self):
        return f"<City name={self.name}>"
