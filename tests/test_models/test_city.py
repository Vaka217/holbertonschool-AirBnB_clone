#!/usr/bin/python3
"""unittest City module."""
import unittest
from models.city import City
from models.base_model import BaseModel


class TestCity(unittest.TestCase):
    """class for test cases related with the City class."""

    def setUp(self):
        """Return class attributes."""
        City.state_id = ""
        City.name = ""

    def test_instance(self):
        """Test if City is instance of BaseModel."""
        my_city = City()
        self.assertTrue(isinstance(my_city, BaseModel))
        self.assertTrue(isinstance(my_city, City))

    def test_has(self):
        """Test if City has all attributes."""
        my_city = City()
        self.assertTrue(hasattr(my_city, "state_id"))
        self.assertTrue(hasattr(my_city, "name"))

    def test_types(self):
        """Test attributes of City."""
        my_city = City()
        self.assertTrue(type(my_city.state_id) == str)
        self.assertTrue(type(my_city.name) == str)

    def test_initialization(self):
        """Test attributes initialization of City object."""
        my_city = City()
        self.assertEqual(my_city.state_id, "")
        self.assertEqual(my_city.name, "")


if __name__ == "__main__":
    unittest.main()
