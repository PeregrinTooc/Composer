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

    def getDate(self, year, imprecise=False, after=False, before=False):
        try:
            result = self._dates[(year, imprecise, after, before)]
        except KeyError:
            result = composerLifeYear(year, imprecise, after, before)
            self._dates[(year, imprecise, after, before)] = result
        return result


class composerLifeYear:

    def __init__(self, year, imprecise, after, before):
        self._year = year
        self._imprecise = imprecise
        self._after = after
        self._before = before


class composerString(str):

    def getYearOfBirth(self):
        dateString = self[: self.find('-')]
        try:
            result = composerFactory.getFactory().getDate(int(dateString))
        except ValueError:
            if dateString.find('um') > -1:
                dateString = dateString[2:]
                result = composerFactory.getFactory().getDate(int(dateString), imprecise=True)
            else:
                dateString = dateString[3:]
                result = composerFactory.getFactory().getDate(int(dateString), before=True)
        return result

    def getYearOfDeath(self):
        dateString = self[(self.find('-')+1):self.find('<')]
        try:
            result = composerFactory.getFactory().getDate(int(dateString))
        except ValueError:
            if dateString.find('um') > -1:
                dateString = dateString[3:]
                result = composerFactory.getFactory().getDate(int(dateString), imprecise=True)
            else:
                dateString = dateString[5:]
                result = composerFactory.getFactory().getDate(int(dateString), after=True)
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
