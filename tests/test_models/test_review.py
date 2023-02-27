#!/usr/bin/python3
""" unittest Review module"""
import unittest
from models.review import Review
from models.base_model import BaseModel


class TestReview(unittest.TestCase):
    """ class for test cases related with the Review class"""

    def setUp(self):
        """ Return class attributes"""
        Review.place_id = ""
        Review.user_id = ""
        Review.text = ""

    def test_instance(self):
        """ Test if Review is instance of BaseModel"""
        my_review = Review()
        self.assertTrue(isinstance(my_review, BaseModel))

    def test_types(self):
        """ Test attributes of Review"""
        my_review = Review()
        self.assertTrue(type(my_review.place_id) == str)
        self.assertTrue(type(my_review.user_id) == str)
        self.assertTrue(type(my_review.text) == str)


if __name__ == "__main__":
    unittest.main()
