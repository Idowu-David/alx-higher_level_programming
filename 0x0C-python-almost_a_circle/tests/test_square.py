#!/usr/bin/python3
"""the `test_rectangle` module"""


import unittest
import os
import json
from models.square import Square
from models.rectangle import Rectangle
from models.rectangle import Base


class TestBase(unittest.TestCase):
    """tests the Base class"""
    def setUp(self):
        """Reset ID counter before each test"""
        Base._Base__nb_objects = 0
        try:
            os.remove("Square.json")
        except FileNotFoundError:
            pass

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

    def test_create(self):
        """test create method"""
        s = Square.create(id=89)
        self.assertIsInstance(s, Square)
        self.assertEqual(s.id, 89)
        self.assertEqual(s.size, 1)
        self.assertEqual(s.x, 0)
        self.assertEqual(s.y, 0)

    def test_create_with_id_and_size(self):
        s = Square.create(id=89, size=1)
        self.assertIsInstance(s, Square)
        self.assertEqual(s.id, 89)
        self.assertEqual(s.size, 1)
        self.assertEqual(s.x, 0)  # default
        self.assertEqual(s.y, 0)  # default

    def test_create_with_id_only(self):
        s = Square.create(id=89)
        self.assertEqual(s.id, 89)
        self.assertEqual(s.size, 1)

    def test_create_with_id_and_size(self):
        s = Square.create(id=89, size=1)
        self.assertEqual(s.id, 89)
        self.assertEqual(s.size, 1)

    def test_create_with_all_attrs(self):
        s = Square.create(id=89, size=1, x=2, y=3)
        self.assertEqual(s.id, 89)
        self.assertEqual(s.size, 1)
        self.assertEqual(s.x, 2)
        self.assertEqual(s.y, 3)

    def tearDown(self):
        # Clean up after tests
        try:
            os.remove("Square.json")
        except FileNotFoundError:
            pass

    def test_load_from_file_when_file_exists(self):
        # Create some Square instances and save them to file
        s1 = Square(5, 1, 2, 10)
        s2 = Square(3, 0, 0, 20)
        Square.save_to_file([s1, s2])

        # Now load from file
        loaded_squares = Square.load_from_file()

        self.assertEqual(len(loaded_squares), 2)
        self.assertTrue(all(isinstance(s, Square) for s in loaded_squares))

        # Check if attributes match
        self.assertEqual(loaded_squares[0].size, 5)
        self.assertEqual(loaded_squares[0].x, 1)
        self.assertEqual(loaded_squares[0].y, 2)
        self.assertEqual(loaded_squares[0].id, 10)

        self.assertEqual(loaded_squares[1].size, 3)
        self.assertEqual(loaded_squares[1].x, 0)
        self.assertEqual(loaded_squares[1].y, 0)
        self.assertEqual(loaded_squares[1].id, 20)

    def test_save_to_file(self):
        s = Square(1)
        Square.save_to_file([s])

        # Check if file was created
        self.assertTrue(os.path.exists("Square.json"))

        # Verify file content
        with open("Square.json", "r") as f:
            content = f.read()
            list_dicts = json.loads(content)

        # The file content should be a list with one dictionary representing s
        self.assertIsInstance(list_dicts, list)
        self.assertEqual(len(list_dicts), 1)
        self.assertEqual(list_dicts[0]['id'], s.id)
        self.assertEqual(list_dicts[0]['size'], s.size)
        self.assertEqual(list_dicts[0]['x'], s.x)
        self.assertEqual(list_dicts[0]['y'], s.y)

    def test_save_empty_list(self):
        Square.save_to_file([])  # Save an empty list
        # Check if the file was created
        self.assertTrue(os.path.exists("Square.json"))
        
        # Read the content to confirm it's an empty JSON list
        with open("Square.json", "r") as f:
            content = f.read()
        
        self.assertEqual(content, "[]")

    def test_save_none(self):
        Square.save_to_file(None)  # Save None instead of list
        
        # Check if file is created
        self.assertTrue(os.path.exists("Square.json"))
        
        # Check that the file content is "[]"
        with open("Square.json", "r") as f:
            content = f.read()
        self.assertEqual(content, "[]")


if __name__ == '__main__':
    unittest.main()
