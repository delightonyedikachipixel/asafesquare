import unittest

def length(word):
    return len(word)

class TestLengthFunction(unittest.TestCase):

    def test_length_regular(self):
        result = length("tech")
        self.assertEqual(result, 4)
        self.assertNotEqual(result, 0)

    def test_length_empty(self):
        result = length("")
        self.assertEqual(result, 0)
        self.assertNotEqual(result, 1)
