#!/usr/bin/python3
""" unittest Amenity module"""
import unittest
from models.amenity import Amenity
from models.base_model import BaseModel


class TestAmenity(unittest.TestCase):
    """ class for test cases related with the Amenity class"""

    def setUp(self):
        """ Return class attributes"""
        Amenity.name = ""

    def test_instance(self):
        """ Test if Amenity is instance of BaseModel"""
        my_Amenity = Amenity()
        self.assertTrue(isinstance(my_Amenity, BaseModel))

    def test_types(self):
        """ Test attributes of Amenity"""
        my_Amenity = Amenity()
        self.assertTrue(type(my_Amenity.name) == str)


if __name__ == "__main__":
    unittest.main()
