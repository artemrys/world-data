from google.cloud import firestore


class City(object):
    def __init__(self,
                 name: str,
                 coordinates: firestore.GeoPoint,
                 country_ref: firestore.DocumentReference):
        self.name = name
        self.coordinates = coordinates
        self.country_ref = country_ref

    @classmethod
    def from_dict(cls, source):
        return City(
            source["name"],
            source["coordinates"],
            source["country"])

    def to_dict(self):
        return {
            "name": self.name,
            "latitude": self.coordinates.latitude,
            "longitude": self.coordinates.longitude,
        }
