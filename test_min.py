import unittest
from min import min_num  

class TestMinNum(unittest.TestCase):

    def test_normal_numbers(self):
        self.assertEqual(min_num("3 5 7 2 9"), 2)

    def test_single_number(self):
        self.assertEqual(min_num("42"), 42)

    def test_invalid_input(self):
        self.assertEqual(min_num("3 a 5"), "Error: Input must contain only numbers.")


