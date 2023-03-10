#!/usr/bin/python3
"""unittest State module."""
import unittest
from models.state import State
from models.base_model import BaseModel


class TestState(unittest.TestCase):
    """class for test cases related with the State class."""

    def setUp(self):
        """Return class attributes."""
        my_state = State()
        my_state.name = ""

    def test_instance(self):
        """Test if State is instance of BaseModel."""
        my_state = State()
        self.assertTrue(isinstance(my_state, BaseModel))
        self.assertTrue(isinstance(my_state, State))

    def test_has(self):
        """Test if State has all attributes."""
        my_state = State()
        self.assertTrue(hasattr(my_state, "name"))

    def test_types(self):
        """Test attributes of State."""
        my_state = State()
        self.assertTrue(type(my_state.name) == str)

    def test_initialization(self):
        """Test attributes initialization of Review object."""
        my_state = State()
        self.assertEqual(my_state.name, "")


if __name__ == "__main__":
    unittest.main()
