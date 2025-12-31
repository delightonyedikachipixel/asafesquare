import unittest
from square import squared_list   

class TestSquaredList(unittest.TestCase):

    def test_basic_numbers(self):
        result = squared_list("1 2 3 4")
        self.assertEqual(result, [1, 4, 9, 16])

    def test_single_number(self):
        result = squared_list("5")
        self.assertEqual(result, [25])

 

    

 

