#!/usr/bin/python3
"""unittest Place module."""
import unittest
from models.place import Place
from models.base_model import BaseModel


class TestPlace(unittest.TestCase):
    """class for test cases related with the Place class."""

    def setUp(self):
        """Return class attributes."""
        my_place = Place()
        my_place.city_id = ""
        my_place.user_id = ""
        my_place.name = ""
        my_place.description = ""
        my_place.number_rooms = 0
        my_place.number_bathrooms = 0
        my_place.max_guest = 0
        my_place.price_by_night = 0
        my_place.latitude = 0.0
        my_place.longitude = 0.0
        my_place.amenity_ids = []

    def test_instance(self):
        """Test if Place is instance of BaseModel."""
        my_place = Place()
        self.assertTrue(isinstance(my_place, BaseModel))
        self.assertTrue(isinstance(my_place, Place))

    def test_has(self):
        """Test if Place has all attributes."""
        my_place = Place()
        self.assertTrue(hasattr(my_place, "city_id"))
        self.assertTrue(hasattr(my_place, "user_id"))
        self.assertTrue(hasattr(my_place, "name"))
        self.assertTrue(hasattr(my_place, "description"))
        self.assertTrue(hasattr(my_place, "number_rooms"))
        self.assertTrue(hasattr(my_place, "number_bathrooms"))
        self.assertTrue(hasattr(my_place, "max_guest"))
        self.assertTrue(hasattr(my_place, "price_by_night"))
        self.assertTrue(hasattr(my_place, "latitude"))
        self.assertTrue(hasattr(my_place, "longitude"))
        self.assertTrue(hasattr(my_place, "amenity_ids"))

    def test_types(self):
        """Test attributes of Place."""
        my_place = Place()
        self.assertTrue(type(my_place.city_id) == str)
        self.assertTrue(type(my_place.user_id) == str)
        self.assertTrue(type(my_place.name) == str)
        self.assertTrue(type(my_place.description) == str)
        self.assertTrue(type(my_place.number_rooms) == int)
        self.assertTrue(type(my_place.number_bathrooms) == int)
        self.assertTrue(type(my_place.max_guest) == int)
        self.assertTrue(type(my_place.price_by_night) == int)
        self.assertTrue(type(my_place.latitude) == float)
        self.assertTrue(type(my_place.longitude) == float)
        self.assertTrue(type(my_place.amenity_ids) == list)

    def test_initialization(self):
        """Test attributes initialization of Place object."""
        my_place = Place()
        self.assertEqual(my_place.city_id, "")
        self.assertEqual(my_place.user_id, "")
        self.assertEqual(my_place.name, "")
        self.assertEqual(my_place.description, "")
        self.assertEqual(my_place.number_rooms, 0)
        self.assertEqual(my_place.number_bathrooms, 0)
        self.assertEqual(my_place.max_guest, 0)
        self.assertEqual(my_place.price_by_night, 0)
        self.assertEqual(my_place.latitude, 0.0)
        self.assertEqual(my_place.longitude, 0.0)
        self.assertEqual(my_place.amenity_ids, [])


if __name__ == "__main__":
    unittest.main()
