class City(object):
    def __init__(self, name, country_ref):
        self.name = name
        self.country_ref = country_ref

    @classmethod
    def from_dict(cls, source):
        return City(source["name"], source["country"])

    def to_dict(self):
        return {
            "name": self.name,
        }
