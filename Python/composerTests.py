import unittest
from composer import composerString
from composer import composerFactory
from composer import composer


class commonTests(unittest.TestCase):
    def setUp(self):
        self.composerFactory = composerFactory.getFactory()
        self.getDate = self.composerFactory.getDate


class getYearOfBirth(commonTests):
    def test_OneSimpleYear(self):
        cut = composerString('1098 - 1179')
        expected = self.composerFactory.getDate('1098')
        actual = cut.getYearOfBirth()
        self.assertEqual(actual, expected)

    def test_AnotherSimpleYear(self):
        cut = composerString('1099 - 1179')
        expected = self.composerFactory.getDate('1099')
        actual = cut.getYearOfBirth()
        self.assertEqual(actual, expected)

    def test_ImpreciseYear(self):
        cut = composerString('um 1050 - 1120')
        expected = self.composerFactory.getDate('1050', True)
        actual = cut.getYearOfBirth()
        self.assertEqual(actual, expected)

    def test_beforeYear(self):
        cut = composerString('vor 1400 - 1474')
        expected = self.composerFactory.getDate('1400', before=True)
        actual = cut.getYearOfBirth()
        self.assertEqual(actual, expected)


class getYearOfDeath(commonTests):
    def test_OneSimpleYear(self):
        cut = composerString('1098-1179 <a ')
        actual = cut.getYearOfDeath()
        expected = self.composerFactory.getDate('1179')
        self.assertEqual(actual, expected)

    def test_AnotherSimpleYear(self):
        cut = composerString('1098-1178 <a ')
        actual = cut.getYearOfDeath()
        expected = self.composerFactory.getDate('1178')
        self.assertEqual(actual, expected)

    def test_ImpreciseYear(self):
        cut = composerString('um 1150 - um 1201 <')
        actual = cut.getYearOfDeath()
        expected = self.composerFactory.getDate('1201', True)
        self.assertEqual(actual, expected)

    def test_AfterYear(self):
        cut = composerString('um 1455 - nach 1517 <a')
        actual = cut.getYearOfDeath()
        expected = self.composerFactory.getDate('1517', after=True)
        self.assertEqual(actual, expected)


class composerLifeYearToString(commonTests):
    def testPreciseDate(self):
        cut = self.getDate(1000)
        self.assertEqual(cut.toString(), '1000')

    def testImpreciseDate(self):
        cut = self.getDate(1000, imprecise=True)
        self.assertEqual(cut.toString(), 'um 1000')

    def testAfterDate(self):
        cut = self.getDate(1000, after=True)
        self.assertEqual(cut.toString(), 'nach 1000')

    def testBeforeDate(self):
        cut = self.getDate(1000, before=True)
        self.assertEqual(cut.toString(), 'vor 1000')


class getName(unittest.TestCase):
    def test_OneName(self):
        cut = composerString('1098-1179 <a href="/wiki/Hildegard_von_Bingen" title="Hildegard von Bingen">Hildegard von Bingen')
        actual = cut.getName()
        expected = "Hildegard von Bingen"
        self.assertEqual(actual, expected)

    def test_AnotherName(self):
        cut = composerString('1831-1907 <a href="/wiki/Joseph_Joachim" title="Joseph Joachim">Joseph Joachim')
        actual = cut.getName()
        expected = "Joseph Joachim"
        self.assertEqual(actual, expected)


class getURL(unittest.TestCase):
    def test_OneURL(self):
        cut = composerString('1098-1179 <a href="/wiki/Hildegard_von_Bingen" title="Hildegard von Bingen">Hildegard von Bingen')
        actual = cut.getURL()
        expected = 'https://de.wikipedia.org/wiki/Hildegard_von_Bingen'
        self.assertEqual(actual, expected)

    def test_AnotherURL(self):
        cut = composerString('1831-1907 <a href="/wiki/Joseph_Joachim" title="Joseph Joachim">Joseph Joachim')
        actual = cut.getURL()
        expected = 'https://de.wikipedia.org/wiki/Joseph_Joachim'
        self.assertEqual(actual, expected)


class toJson(unittest.TestCase):
    def test_OneString(self):
        composerStringRepr = composerString('1831-1907 <a href="/wiki/Joseph_Joachim" title="Joseph Joachim">Joseph Joachim')
        cut = composer(composerStringRepr)
        actual = cut.toJson()
        expected = '{"name":"Joseph Joachim","yearOfBirth":"1831","yearOfDeath":"1907","wikiLink":"https://de.wikipedia.org/wiki/Joseph_Joachim"}'
        self.assertEqual(actual, expected)

    def test_anotherString(self):
        composerStringRepr = composerString('um 1831 - nach 1907 <a href="/wiki/Joseph_Joachim" title="Joseph Joachim">Joseph Joachim')
        cut = composer(composerStringRepr)
        actual = cut.toJson()
        expected = '{"name":"Joseph Joachim","yearOfBirth":"um 1831","yearOfDeath":"nach 1907","wikiLink":"https://de.wikipedia.org/wiki/Joseph_Joachim"}'
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
