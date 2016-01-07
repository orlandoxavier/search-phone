import unittest
from search_phone import search_phone, letter_to_number


class SearchPhoneTest(unittest.TestCase):
    def test_search_phone_orlando_xavier(self):
        self.assertTrue(search_phone('ORLANDO-XAVIER') == '6752636-928437')

    def test_search_phone_underscore_orlando_xavier(self):
        self.assertTrue(search_phone('_ORLANDO-XAVIER') == '_6752636-928437')

    def test_search_phone_home_sweet_home(self):
        self.assertTrue(search_phone('1-HOME-SWEET-HOME') == '1-4663-79338-4663')

    def test_search_phone_home_sweet_home(self):
        self.assertTrue(search_phone('MY-MISERABLE-JOB') == '69-647372253-562')


class LetterToNumberTeset(unittest.TestCase):
    def test_letter_to_number_A(self):
        self.assertTrue(letter_to_number('A') == '2')

    def test_letter_to_number_B(self):
        self.assertTrue(letter_to_number('B') == '2')

    def test_letter_to_number_h(self):
        self.assertTrue(letter_to_number('h') == '4')


if __name__ == '__main__':
    unittest.main()