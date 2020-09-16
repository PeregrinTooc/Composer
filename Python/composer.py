import json

class composerFactory:
    __instance = None

    @staticmethod
    def getFactory():
        if composerFactory.__instance is None:
            composerFactory.instance = composerFactory()
        return composerFactory.instance

    def __init__(self):
        self._dates = {}

    def getDate(self, year):
        result = self._dates[year]
        return result


class composerLifeYear:

    def __init__(self, year):
        self.year = year


class composerString(str):

    def getBirthYear(self):
        return composerFactory.getFactory().getDate(int(self[: self.find('-')]))


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
