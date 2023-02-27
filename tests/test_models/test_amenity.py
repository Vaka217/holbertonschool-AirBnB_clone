#!/usr/bin/python3
""" unittest Amenity module"""
import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """ class for test cases related with the Amenity class"""

    def test_amenity(self):
        """ Test all Amenity class attributes"""
        my_amenity = Amenity()
        my_amenity.name = "Spa"
        self.assertEqual(my_amenity.__str__(),
                         f'[{my_amenity.__class__.__name__}] '
                         f'({my_amenity.id}) {my_amenity.__dict__}')
