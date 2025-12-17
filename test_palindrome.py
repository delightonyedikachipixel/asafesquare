from function_class import word_is_palindrome
from unittest import TestCase
def test_that_word_is_palindrome(self):
   
        is_palindrome= word_is_palindrome()
        print(is_palindrome)
        self.assertTrue(is_palindrome)

    def test_word_is_not_palindrome(self):

        is_palindrome = word_is_palindrome()
        self.assertFalse(is_palindrome)
