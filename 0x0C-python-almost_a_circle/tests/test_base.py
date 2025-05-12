#!/usr/bin/python3
"""the `test_base` module"""


import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """tests the Base class"""
    def test_base_class(self):
        """tests the base class"""
        b1 = Base()
        self.assertAlmostEqual(b1.id, 1)
        b2 = Base()
        self.assertEqual(b2.id, 2)
        b3 = Base(12)
        self.assertEqual(b3.id, 12)
        b4 = Base()
        self.assertEqual(b4.id, 3)

  