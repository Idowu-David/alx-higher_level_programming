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
        s = Square(1)
        self.assertEqual(s.size, 1)

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
    
    def test_size_zero_raises(self):
        """tests for 0 input"""
        with self.assertRaises(ValueError) as cm:
            Square(0)
        self.assertEqual(str(cm.exception), "width must be > 0")

    def test_str(self):
        """tests the __str__ method"""
        s = Square(4, 2, 1, 99)
        self.assertEqual(str(s), "[Square] (99) 2/1 - 4")

    def test_update_args(self):
        s = Square(5)
        s.update(10, 7, 2, 3)
        self.assertEqual(str(s), "[Square] (10) 2/3 - 7")

    def test_update_kwargs(self):
        s = Square(5)
        s.update(id=42, size=10, y=7)
        self.assertEqual(str(s), "[Square] (42) 0/7 - 10")

    def test_to_dictionary(self):
        s = Square(10, 2, 1, 1)
        expected = {'id': 1, 'size': 10, 'x': 2, 'y': 1}
        self.assertEqual(s.to_dictionary(), expected)


if __name__ == '__main__':
    unittest.main()
