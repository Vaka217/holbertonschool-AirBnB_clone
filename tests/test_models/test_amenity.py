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
        my_amenity = Amenity()
        self.assertTrue(isinstance(my_amenity, BaseModel))
        self.assertTrue(isinstance(my_amenity, Amenity))

    def test_has(self):
        """ Test if Amenity has all attributes"""
        my_amenity = Amenity()
        self.assertTrue(hasattr(my_amenity, "name"))

    def test_types(self):
        """ Test attributes of Amenity"""
        my_amenity = Amenity()
        self.assertTrue(type(my_amenity.name) == str)

    def test_initialization(self):
        """ Test attributes initialization of Amenity object"""
        my_amenity = Amenity()
        self.assertEqual(my_amenity.name, "")


if __name__ == "__main__":
    unittest.main()
