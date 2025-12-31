import unittest
from sumsquare import square_and_sum  

class TestSumSquare(unittest.TestCase):

    def test_square_and_sum_basic(self):
        result = square_and_sum("1 2 3")
        self.assertEqual(result, 14)

    def test_square_and_sum_single_number(self):
        result = square_and_sum("4")
        self.assertEqual(result, 16)



