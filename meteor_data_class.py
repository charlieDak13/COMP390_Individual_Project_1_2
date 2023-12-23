# This class makes blueprints an object that holds all the fields that each meteor has
class MeteorDataEntry:

    def __init__(self, name, id, nameType, recClass, mass, fall, year, recLat, recLong, geoLocation, states, countries):
        self.name = name
        self.id = id
        self.nameType = nameType
        self.recClass = recClass
        self.mass = mass
        self.fall = fall
        self.year = year
        self.recLat = recLat
        self.recLong = recLong
        self.geoLocation = geoLocation
        self.states = states
        self.countries = countries
