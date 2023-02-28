#!/usr/bin/python3
""" unittest User module"""
import unittest
from models.user import User
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    """ class for test cases related with the User class"""

    def setUp(self):
        """ Return class attributes"""
        User.email = ""
        User.password = ""
        User.first_name = ""
        User.last_name = ""

    def test_instance(self):
        """ Test if User is instance of BaseModel"""
        my_user = User()
        self.assertTrue(isinstance(my_user, BaseModel))

    def test_types(self):
        """ Test attributes of User"""
        my_user = User()
        self.assertTrue(type(my_user.email) == str)
        self.assertTrue(type(my_user.password) == str)
        self.assertTrue(type(my_user.first_name) == str)
        self.assertTrue(type(my_user.last_name) == str)

    def test_initialization(self):
        """ Test attributes initialization of Review object"""
        my_user = User()
        self.assertEqual(my_user.email, "")
        self.assertEqual(my_user.password, "")
        self.assertEqual(my_user.first_name, "")
        self.assertEqual(my_user.last_name, "")


if __name__ == "__main__":
    unittest.main()
