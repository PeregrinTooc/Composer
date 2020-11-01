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

    def createAll(self):
        import os
        script_path = os.path.abspath(__file__) 
        print(script_path)
        
        script_dir = os.path.split(script_path)[0] #i.e. /path/to/dir/
        print(script_dir)

        rel_path = 'composers.json'
        abs_file_path = os.path.join(script_dir, rel_path)
        print(abs_file_path)

        self._composers = {}
        with open(abs_file_path, 'r', encoding="utf8") as source:
            composerJSONs = json.loads(source.read())
        
        for composerJSON in composerJSONs:
            self._composers[composerJSON['name']] = composer(dictRepresentation = composerJSON)

    def displayAll(self):
        for composer in self._composers.values():
            print(composer.toString())       



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
        if self._string != '':
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
    def __init__(self, stringRepresentation = '', dictRepresentation = {}):
        if stringRepresentation != '':
            self._name = stringRepresentation.getName()
            self._YearOfBirth = stringRepresentation.getYearOfBirth()
            self._YearOfDeath = stringRepresentation.getYearOfDeath()
            self._WikiLink = stringRepresentation.getURL()
        else:
            self._name = dictRepresentation['name']
            dateString = dictRepresentation['yearOfBirth'] + ' - ' + dictRepresentation['yearOfDeath']
            self._YearOfBirth = composerString(dateString).getYearOfBirth()
            self._YearOfDeath = composerString(dateString).getYearOfDeath()
            self._WikiLink = dictRepresentation['wikiLink'] 

    def toJson(self):
        return json.dumps(self.toDict())

    def toString(self):
        result = ''
        for k,v in self.toDict().items():
            result += k +':'+v+', '
        result[0:-1]
        return result

    def toDict(self):
        result = {"name": self._name,
                  "yearOfBirth": self._YearOfBirth.toString(),
                  "yearOfDeath": self._YearOfDeath.toString(),
                  "wikiLink": self._WikiLink
             }
        return result

