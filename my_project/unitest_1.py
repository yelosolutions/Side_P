#!/usr/bin/python3
import unittest


class TestAssert(unittest.TestCase):
    """class that inherits from unittest.TestCase"""
    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertFalse('MwN'.isupper())
        self.assertTrue('MAN'.isupper())


if __name__ == '__main__':
    unittest.main()
