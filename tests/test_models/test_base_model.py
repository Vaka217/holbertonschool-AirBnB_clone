#!/usr/bin/python3
""" unittest BaseModel module"""
import unittest
import io
from datetime import datetime
from unittest.mock import patch
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from contextlib import redirect_stdout
import os


class TestBase(unittest.TestCase):
    """ class for test cases related with the BaseModel class"""
    base = BaseModel()

    def setUp(self):
        """ Test file saving"""
        with open("file.json", "w") as f:
            FileStorage.__file_path = 'file.json'
            FileStorage.__objects = {}

    def tearDown(self):
        """ Destroys created file"""
        try:
            os.remove(FileStorage.__file_path)
        except FileNotFoundError:
            pass

    def test_to_dict(self):
        """ Test of BaseModel to_dict() method"""
        dictionary = TestBase.base.to_dict()
        self.assertEqual(dictionary['id'], TestBase.base.id)

    def test_id(self):
        """ Test of BaseModel id attribute"""
        self.assertTrue(isinstance(TestBase.base.id, str))

    def test_created_at(self):
        """ Test of BaseModel created_at attribute"""
        self.assertTrue(isinstance(TestBase.base.created_at, datetime))

    def test_str(self):
        """ Test of BaseModel __str__ method"""
        self.assertEqual(TestBase.base.__str__(),
                         f'[{TestBase.base.__class__.__name__}] '
                         f'({TestBase.base.id}) {TestBase.base.__dict__}')

    def test_kwargs(self):
        """ Test of BaseModel __init__ method with kwargs"""
        kwargs = {'id': "1", 'created_at': "2023-02-28T05:08:35.607604",
                  'updated_at': "2023-02-28T05:08:35.607709"}
        base = BaseModel(**kwargs)
        self.assertEqual(base.id, "1")
        self.assertEqual(base.created_at,
                         datetime(2023, 2, 28, 5, 8, 35, 607604))
        self.assertEqual(base.updated_at,
                         datetime(2023, 2, 28, 5, 8, 35, 607709))

    def test_save(self):
        """ Test of BaseModel save() method"""
        base = BaseModel()
        prev_updated_at = base.updated_at
        base.save()
        self.assertNotEqual(prev_updated_at, base.updated_at)


if __name__ == "__main__":
    unittest.main()
