import unittest
from composer import composerString
from composer import composerFactory

class commonTests(unittest.TestCase):
    def setUp(self):
        self.composerFactory = composerFactory.getFactory()


class getYearOfBirth(commonTests):
    def test_OneSimpleYear(self):
        cut = composerString(str('1098 - 1179'))
        expected = self.composerFactory.getDate(1098)
        actual = cut.getYearOfBirth()
        self.assertEqual(actual, expected)

    def test_AnotherSimpleYear(self):
        cut = composerString(str('1099 - 1179'))
        expected = self.composerFactory.getDate(1099)
        actual = cut.getYearOfBirth()
        self.assertEqual(actual, expected)

    def test_ImpreciseYear(self):
        cut = composerString(str('um 1050 - 1120'))
        expected = self.composerFactory.getDate(1050, True)
        actual = cut.getYearOfBirth()
        self.assertEqual(actual, expected)

    def test_beforeYear(self):
        cut = composerString(str('vor 1400 - 1474'))
        expected = self.composerFactory.getDate(1400, before=True)
        actual = cut.getYearOfBirth()
        self.assertEqual(actual, expected)

class getYearOfDeath(commonTests):
    def test_OneSimpleYear(self):
        cut = composerString(str('1098-1179 <a '))
        actual = cut.getYearOfDeath()
        expected = self.composerFactory.getDate(1179)
        self.assertEqual(actual, expected)

    def test_AnotherSimpleYear(self):
        cut = composerString(str('1098-1178 <a '))
        actual = cut.getYearOfDeath()
        expected = self.composerFactory.getDate(1178)
        self.assertEqual(actual, expected)

    def test_ImpreciseYear(self):
        cut = composerString(str('um 1150 - um 1201 <'))
        actual = cut.getYearOfDeath()
        expected = self.composerFactory.getDate(1201, True)
        self.assertEqual(actual, expected)

    def test_AfterYear(self):
        cut = composerString(str('um 1455 - nach 1517 <a'))
        actual = cut.getYearOfDeath()
        expected = self.composerFactory.getDate(1517, after=True)
        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()
