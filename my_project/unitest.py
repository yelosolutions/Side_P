#!/usr/bin/python3
import unittest


class StringMethodTest(unittest.TestCase):
    """Class that is a subclass of TestCase
    for testing string methods
    """
    def test_upper(self):
        self.assertEqual('man'.upper(), 'MAN')

    def test_lower(self):
        self.assertNotEqual('MAN'.lower(), 'Man')
    def test_isupper(self):
        self.assertTrue('man'.islower())


if __name__ == "__main__":
    unittest.main()
