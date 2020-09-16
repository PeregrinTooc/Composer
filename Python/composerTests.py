import unittest
from composer import composerString

class getBirthyear(unittest.TestCase):

    def test_simpleYear(self):
        cut = composerString(str('1098–1179'))
        actual = cut.getBirthYear()
        self.assertEqual(actual,'1098')

    def test_simpleYear(self):
        cut = composerString(str('1099–1179'))
        actual = cut.getBirthYear()
        self.assertEqual(actual,'1099')


if __name__ == 'main':
    unittest.main()
