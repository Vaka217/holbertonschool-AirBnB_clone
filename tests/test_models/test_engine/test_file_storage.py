#!/usr/bin/python3
""" unittest FileStorage module"""
import unittest
import io
from datetime import datetime
from unittest.mock import patch
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from contextlib import redirect_stdout
from pathlib import Path
import os
from models import storage
import json


class TestFileStorage(unittest.TestCase):
    """ class for test cases related with the FileStorage class"""

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

    def test_file_path(self):
        """ Test for FileStorage __file_path attribute"""
        path = Path('file.json')
        assert path.is_file()

    def test_objects(self):
        """ Test for FileStorage __objects attribute"""
        self.assertEqual(FileStorage.__objects, {})

    def test_all(self):
        """ Test for FileStorage all() method"""
        fileobj = FileStorage()
        filedict = fileobj.all()
        self.assertTrue(type(filedict) == dict)

    def test_new(self):
        """ Test for FileStorage new() method"""
        fileobj = FileStorage()
        baseobj = BaseModel()
        fileobj.new(baseobj)
        key = f'{baseobj.__class__.__name__}.{baseobj.id}'
        self.assertTrue(key in fileobj.all())

    def test_save(self):
        """ Test for FileStorage save() method"""
        baseobj = BaseModel()
        baseobj.save()
        storage.save()
        with open('file.json') as f:
            dict_save = json.load(f)
            self.assertEqual(baseobj.to_dict(),
                             dict_save.get(f'BaseModel.{baseobj.id}'))

    def test_reload(self):
        """ Test for FileStorage reload() method when empty"""
        fileobj = FileStorage()
        baseobj = BaseModel()
        fileobj.new(baseobj)
        fileobj.save()
        prev_dict = fileobj.all()
        os.remove('file.json')
        fileobj.reload()
        new_dict = fileobj.all()
        self.assertTrue(prev_dict == new_dict)


if __name__ == "__main__":
    unittest.main()
