class composer:
    def init(self, name):
        self.name = name

    def setYearOfBirth(self, year, isExact=True):
        self.YearOfBirth = (year, isExact)

    def setYearofDeath(self, year, isExact=True):
        self.YearOfDeath = (year, isExact)

    def setWikiLink(self, link):
        self.WikiLink = link
