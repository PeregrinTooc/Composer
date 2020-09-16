import json


class composerFactory:
    _instance = None

    @staticmethod
    def getFactory():
        if composerFactory._instance is None:
            composerFactory._instance = composerFactory()
        return composerFactory._instance

    def __init__(self):
        self._dates = {}

    def getDate(self, year, imprecise=False):
        try:
            result = self._dates[(year, imprecise)]
        except KeyError:
            result = composerLifeYear(year, imprecise)
            self._dates[(year, imprecise)] = result
        return result


class composerLifeYear:

    def __init__(self, year, imprecise):
        self._year = year
        self._imprecise = imprecise


class composerString(str):

    def getBirthYear(self):
        dateString = self[: self.find('-')]
        try:
            result = composerFactory.getFactory().getDate(int(dateString))
        except ValueError:
            dateString = dateString[2:]
            result = composerFactory.getFactory().getDate(int(dateString), True)
        return result


class composer:
    def __init__(self, name):
        self.name = name

    def setYearOfBirth(self, year, isExact=True):
        self.YearOfBirth = (year, isExact)

    def setYearofDeath(self, year, isExact=True):
        self.YearOfDeath = (year, isExact)

    def setWikiLink(self, url):
        self.WikiLink = url

    def toJson(self):
        return None
