#!/usr/bin/python3
""" unittest User module"""
import unittest
from models.user import User


class TestUser(unittest.TestCase):
    """ class for test cases related with the User class"""

    def test_user(self):
        """ Test all User class attributes"""
        my_user = User()
        my_user.first_name = "Betty"
        my_user.last_name = "Bar"
        my_user.email = "airbnb@mail.com"
        my_user.password = "root"
        self.assertEqual(my_user.__str__(),
                         f'[{my_user.__class__.__name__}] '
                         f'({my_user.id}) {my_user.__dict__}')
