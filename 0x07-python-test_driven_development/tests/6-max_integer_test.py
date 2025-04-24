#!/usr/bin/python3
"""This module provides a Unit Test for the function `max_integer`"""


import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """
    This class contains methods to test the max_integer function
    """
    def test_function(self):
        """test that the function returns the max integer in the list"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, -2, 0, -4]), 1)
        self.assertEqual(max_integer([-10, -20, 0, -40]), 0)
        self.assertEqual(max_integer([1.2, -2.9, 0.3, -4.5]), 1.2)
        self.assertEqual(max_integer([3]), 3)

    def test_input(self):
        """test that the input is an integer or float"""
        with self.assertRaises(ValueError):
            max_integer([1, "2", 4, 5])
        with self.assertRaises(ValueError):
            max_integer([1, (3, 4), 5])
    
    def test_raises(self):
        """test that an exception was raised if the argument is not a list"""
        with self.assertRaises(TypeError):
            max_integer((3, 4, 5))
        with self.assertRaises(TypeError):
            max_integer("3, 4, 5")
      
if __name__ == '__main__':
    unittest.main()
