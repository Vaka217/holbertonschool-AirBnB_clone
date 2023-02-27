#!/usr/bin/python3
""" unittest State module"""
import unittest
from models.state import State


class TestState(unittest.TestCase):
    """ class for test cases related with the State class"""

    def test_state(self):
        """ Test all State class attributes"""
        my_state = State()
        my_state.name = "Texas"
        self.assertEqual(my_state.__str__(),
                         f'[{my_state.__class__.__name__}] '
                         f'({my_state.id}) {my_state.__dict__}')
