import unittest
from composer import composerString
from composer import composerFactory


class getBirthyear(unittest.TestCase):

    def setUp(self):
        self.composerFactory = composerFactory()

    def test_OneSimpleYear(self):
        cut = composerString(str('1098-1179'))
        actual = cut.getBirthYear()
        expected = self.composerFactory.getDate(1098)
        self.assertEqual(actual, expected)

    def test_AnotherSimpleYear(self):
        cut = composerString(str('1099-1179'))
        actual = cut.getBirthYear()
        expected = self.composerFactory.getDate(1099)
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
