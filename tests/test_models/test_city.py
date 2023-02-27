#!/usr/bin/python3
""" unittest City module"""
import unittest
from models.city import City
from models.state import State


class TestCity(unittest.TestCase):
    """ class for test cases related with the City class"""

    def test_city(self):
        """ Test all City class attributes"""
        my_city = City()
        my_state = State()
        my_city.state_id = my_state.id
        my_city.name = "Montevideo"
        self.assertEqual(my_city.__str__(),
                         f'[{my_city.__class__.__name__}] '
                         f'({my_city.id}) {my_city.__dict__}')
