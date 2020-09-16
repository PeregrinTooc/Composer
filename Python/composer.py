import json

class composerString(str):
    def init(self, string):
        self = string

    def getBirthYear(self):
        return self[ 0 : super().find('-') ]



class composer:
    def init(self, name):
        self.name = name

    def setYearOfBirth(self, year, isExact=True):
        self.YearOfBirth = (year, isExact)

    def setYearofDeath(self, year, isExact=True):
        self.YearOfDeath = (year, isExact)

    def setWikiLink(self, url):
        self.WikiLink = url

    def toJson(self):
        return none
