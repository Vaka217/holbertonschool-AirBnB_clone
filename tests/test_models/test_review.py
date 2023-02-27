#!/usr/bin/python3
""" unittest Review module"""
import unittest
from models.review import Review
from models.place import Place
from models.user import User


class TestReview(unittest.TestCase):
    """ class for test cases related with the Review class"""

    def test_review(self):
        """ Test all Review class attributes"""
        my_review = Review()
        my_place = Place()
        my_user = User()
        my_review.place_id = my_place.id
        my_review.user_id = my_user.id
        my_review.text = "Tremendo lugar"
        self.assertEqual(my_review.__str__(),
                         f'[{my_review.__class__.__name__}] '
                         f'({my_review.id}) {my_review.__dict__}')
