import unittest
from len import max_num  

class TestMaxNum(unittest.TestCase):

    def test_normal_numbers(self):
        self.assertEqual(max_num("3 5 7 2 9"), 9)

    
    def test_empty_input(self):
        self.assertEqual(max_num(""), "Error: Please enter only numbers separated by spaces.")


