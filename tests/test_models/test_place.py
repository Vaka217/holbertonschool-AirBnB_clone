#!/usr/bin/python3
""" unittest Place module"""
import unittest
from models.place import Place
from models.city import City
from models.user import User
from models.amenity import Amenity


class TestPlace(unittest.TestCase):
    """ class for test cases related with the Place class"""

    def test_place(self):
        """ Test all Place class attributes"""
        my_place = Place()
        my_city = City()
        my_user = User()
        my_amenity = Amenity()
        my_place.city_id = my_city.id
        my_place.user_id = my_user.id
        my_place.name = "Bahamas Resort"
        my_place.description = "Buenazo"
        my_place.number_rooms = 10
        my_place.number_bathrooms = 8
        my_place.max_guest = 89
        my_place.price_by_night = 12
        my_place.latitude = 27.5
        my_place.longitude = 49.3
        my_place.amenity_ids = my_amenity.id
        self.assertEqual(my_place.__str__(),
                         f'[{my_place.__class__.__name__}] '
                         f'({my_place.id}) {my_place.__dict__}')
