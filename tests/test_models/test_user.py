#!/usr/bin/python3
""" unittest User module"""
import unittest
from models.user import User
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    """ class for test cases related with the User class"""

    def setUp(self):
        """Return class attributes."""
        my_user = User()
        my_user.email = ""
        my_user.password = ""
        my_user.first_name = ""
        my_user.last_name = ""

    def test_instance(self):
        """Test if User is instance of BaseModel."""
        my_user = User()
        self.assertTrue(isinstance(my_user, BaseModel))
        self.assertTrue(isinstance(my_user, User))

    def test_has(self):
        """Test if User has all attributes."""
        my_user = User()
        self.assertTrue(hasattr(my_user, "email"))
        self.assertTrue(hasattr(my_user, "password"))
        self.assertTrue(hasattr(my_user, "first_name"))
        self.assertTrue(hasattr(my_user, "last_name"))

    def test_types(self):
        """Test attributes of User."""
        my_user = User()
        self.assertTrue(type(my_user.email) == str)
        self.assertTrue(type(my_user.password) == str)
        self.assertTrue(type(my_user.first_name) == str)
        self.assertTrue(type(my_user.last_name) == str)

    def test_initialization(self):
        """Test attributes initialization of Review object."""
        my_user = User()
        self.assertEqual(my_user.email, "")
        self.assertEqual(my_user.password, "")
        self.assertEqual(my_user.first_name, "")
        self.assertEqual(my_user.last_name, "")


if __name__ == "__main__":
    unittest.main()
