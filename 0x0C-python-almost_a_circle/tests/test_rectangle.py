#!/usr/bin/python3
"""the `test_rectangle` module"""


import unittest
from models.rectangle import Rectangle
from models.rectangle import Base


class TestBase(unittest.TestCase):
    """tests the Base class"""
    def setUp(self):
        """Reset ID counter before each test"""
        Base._Base__nb_objects = 0
    
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

    def test_raises(self):
        """tests if appropriate exceptions are raised"""
        with self.assertRaises(TypeError):
            Rectangle("4", 4, 2, 1)
        with self.assertRaises(ValueError):
            Rectangle(-3, 4, 3, 2)
        with self.assertRaises(TypeError):
            Rectangle(4, "3", 2, 1)
        with self.assertRaises(ValueError):
            Rectangle(3, -4, 3, 2)
        with self.assertRaises(TypeError):
            Rectangle(2, 4, "2", 1)
        with self.assertRaises(ValueError):
            Rectangle(3, 4, -3, 2)
        with self.assertRaises(TypeError):
            Rectangle(4, 4, 2, "1")
        with self.assertRaises(ValueError):
            Rectangle(3, 4, 3, -2)


if __name__ == '__main__':
    unittest.main()
