#!/usr/bin/python3
"""
Unit tests for the Base class in the models.base module.

This module contains test cases to validate the functionality of the Base class,
specifically its automatic ID assignment and manual ID setting.

Classes:
    TestBase: Inherits from unittest.TestCase and contains methods to test
              various behaviors of the Base class.

Usage:
    Run this module with a test runner like unittest or pytest to verify the
    correctness of the Base class implementation.

Example:
    $ python -m unittest test_base.py
"""


import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """
    Unit tests for the Base class.

    This test case verifies the behavior of the Base class, particularly
    its automatic ID assignment and handling of user-defined IDs
    """

    def setUp(self):
        """Reset class-level counter before each test"""
        Base._Base__nb_objects = 0

    def test_base_class(self):
        """
        Test automatic and manual ID assignment in Base instances

        - When no ID is provide, the Base class should auto-increment
        - When an ID is manually specified, it should override the
        auto-assigned one.
        """
        b1 = Base()
        self.assertEqual(b1.id, 1)
        b2 = Base()
        self.assertEqual(b2.id, 2)
        b3 = Base(12)
        self.assertEqual(b3.id, 12)
        b4 = Base()
        self.assertEqual(b4.id, 3)
