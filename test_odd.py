import unittest
from odd import remove_odd 
class TestRemoveOdd(unittest.TestCase):

    def test_basic_string(self):
        self.assertEqual(remove_odd("abcdefgh"), "aceg")

    def test_numbers_in_string(self):
        self.assertEqual(remove_odd("123456"), "135")

