#!/usr/bin/python3
"""the `test_rectangle` module"""


import unittest
from models.rectangle import Rectangle
from models.rectangle import Base


class TestBase(unittest.TestCase):
    """tests the Base class"""
    def test_rectangle(self):
        """tests basics inheritance of rectangle"""
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.id, 1)
        r2 = Rectangle(2, 10)
        self.assertEqual(r2.id, 2)
        r3 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r3.id, 12)

    def test_rectangle_inheritance(self):
        """tests the inheritance of rectangle from base class"""
        self.assertTrue(issubclass(Rectangle, Base))

  
if __name__ == '__main__':
    unittest.main()