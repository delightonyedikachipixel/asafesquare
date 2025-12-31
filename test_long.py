import unittest
from long import longest_word   

class TestLongestWord(unittest.TestCase):

    def test_longest_word_basic(self):
        result = longest_word("apple banana mango")
        self.assertEqual(result, "banana.6")

    def test_longest_word_single_word(self):
        result = longest_word("orange")
        self.assertEqual(result, "orange.6")

    
