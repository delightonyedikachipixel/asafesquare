import unittest
from ing import add_ing


class TestAddIng(unittest.TestCase):

    def test_word_less_than_three_characters(self):
        self.assertEqual(add_ing("go"), "go")

    def test_word_without_ing(self):
        self.assertEqual(add_ing("play"), "playing")

    def test_word_with_ing(self):
        self.assertEqual(add_ing("playing"), "playingly")


 
