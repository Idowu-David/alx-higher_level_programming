#!/usr/bin/python3
"""the `test_rectangle` module"""


import unittest
from models.square import Square
from models.rectangle import Rectangle
from models.rectangle import Base


class TestBase(unittest.TestCase):
    """tests the Base class"""
    def setUp(self):
        """Reset ID counter before each test"""
        Base._Base__nb_objects = 0

    def test_square(self):
        """tests basics inheritance of rectangle"""
        s1 = Square(1)
        self.assertEqual(s1.id, 1)
        s2 = Square(1, 3)
        self.assertEqual(s2.id, 2)
        s3 = Square(1, 2, 3)
        self.assertEqual(s3.id, 3)
        s4 = Square(1, 2, 3, 12)
        self.assertEqual(s4.id, 12)

    def test_rectangle_inheritance(self):
        """tests the inheritance of rectangle from base class"""
        self.assertTrue(issubclass(Square, Rectangle))

    def test_raises(self):
        """tests if appropriate exceptions are raised"""
        with self.assertRaises(TypeError):
            Square("4", 4, 2, 1)
        with self.assertRaises(ValueError):
            Square(-3, 4, 3, 2)
        with self.assertRaises(TypeError):
            Square(4, "3", 2, 1)
        with self.assertRaises(ValueError):
            Square(3, -4, 3, 2)
        with self.assertRaises(TypeError):
            Square(2, 4, "2", 1)
        with self.assertRaises(ValueError):
            Square(3, 4, -3, 2)


if __name__ == '__main__':
    unittest.main()
