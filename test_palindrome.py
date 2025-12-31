import unittest
from palindrome import is_prime_and_palindrome  

class TestPrimeAndPalindrome(unittest.TestCase):

    def test_prime_and_palindrome(self):
        self.assertTrue(is_prime_and_palindrome(131))  

    def test_not_prime(self):
        self.assertFalse(is_prime_and_palindrome(121))  

    def test_not_palindrome(self):
        self.assertFalse(is_prime_and_palindrome(13))   

    
