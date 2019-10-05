#!/usr/bin/python3
"""
===================================
Module for max_integer() function
===================================
"""


import unittest

max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Method for find a max integer in a list"""

    def test_basic_oneelement(self):
        """test with only one element"""
        self.assertEqual(max_integer([1]), 1)

    def test_max_integer(self):
        """ positives numbers like arguments"""
        self.assertEqual(max_integer([7, 22, 3, 4]), 22)

    def test_max_integer_negative(self):
        """negatives numbers like arguments"""
        self.assertEqual(max_integer([-12, -22, -3, 0]), 0)

    def test_characters(self):
        """test empty arguments"""
        self.assertEqual(max_integer([]), '')

    def test_characters(self):
        """test with characters like arguments"""
        self.assertEqual(max_integer(['M', 'i', 'g', 'u', 'e', 'l']), 'u')

    def test_for_None_argument(self):
        """test None argument"""
        self.assertEqual(max_integer([]), None)
