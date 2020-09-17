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
        self._string = ''
        self._qualifier = ''

    def toString(self):
        self._string = str(self._year)
        self._addQualifierIfApplicable()
        return self._string

    def _addQualifierIfApplicable(self):
        self._qualifier = ''
        self._determineQualifier()
        self._string = self._qualifier + self._string

    def _determineQualifier(self):
        if self._imprecise:
            self._qualifier = 'um '
        elif self._after:
            self._qualifier = 'nach '
        elif self._before:
            self._qualifier = 'vor '


class composerString(str):

    def __init__(self, string):
        self._getDate = composerFactory.getFactory().getDate

    def getYearOfBirth(self):
        dateString = self[: self.find('-')]
        dateString = dateString.replace(' ', '')
        try:
            int(dateString)
        except ValueError:
            if dateString.find('um') > -1:
                dateString = dateString[2:]
                result = self._getDate(dateString, imprecise=True)
            elif dateString.find('/') > -1:
                result = self._getDate(dateString)
            else:
                dateString = dateString[3:]
                result = self._getDate(dateString, before=True)
        else:
            result = self._getDate(dateString)
        return result

    def getYearOfDeath(self):
        dateString = self[(self.find('-')+1):self.find('<')]
        dateString = dateString.replace(' ', '')
        try:
            int(dateString)
        except ValueError:
            if dateString.find('um') > -1:
                dateString = dateString[2:]
                result = self._getDate(dateString, imprecise=True)
            elif dateString.find('/') > -1:
                result = self._getDate(dateString)
            else:
                dateString = dateString[4:]
                result = self._getDate(dateString, after=True)
        else:
            result = self._getDate(dateString)
        return result

    def getName(self):
        result = self[self.find(">")+1:]
        return result

    def getURL(self):
        endpoint = self[self.find('href="')+6:self.find('" title')]
        result = 'https://de.wikipedia.org'+endpoint
        return result


class composer:
    def __init__(self, composerString):
        self._name = composerString.getName()
        self._YearOfBirth = composerString.getYearOfBirth()
        self._YearOfDeath = composerString.getYearOfDeath()
        self._WikiLink = composerString.getURL()

    def toJson(self):
        result = '{'
        result += '"name":"'+self._name+'",'
        result += '"yearOfBirth":"'+self._YearOfBirth.toString()+'",'
        result += '"yearOfDeath":"'+self._YearOfDeath.toString()+'",'
        result += '"wikiLink":"'+self._WikiLink+'"'
        result += '}'
        return result
