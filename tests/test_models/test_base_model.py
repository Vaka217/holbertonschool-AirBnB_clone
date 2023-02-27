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
        TestBase.base.id = "xd"
        self.assertEqual(TestBase.base.id, "xd")

    def test_created_at(self):
        """ Test of BaseModel created_at attribute"""
        time = datetime.now()
        TestBase.base.created_at = time
        self.assertEqual(TestBase.base.created_at, time)

    def test_str(self):
        """ Test of BaseModel __str__ method"""
        self.assertEqual(TestBase.base.__str__(),
                         f'[{TestBase.base.__class__.__name__}] '
                         f'({TestBase.base.id}) {TestBase.base.__dict__}')

    def test_kwargs(self):
        """ Test of BaseModel __init__ method with kwargs"""
        TestBase.base.id = "Juan"
        TestBase.base.number = 89
        self.assertEqual(TestBase.base.__str__(),
                         f'[{TestBase.base.__class__.__name__}] '
                         f'(Juan) {TestBase.base.__dict__}')

    def test_save_self(self):
        """ Test of BaseModel save(self) method"""
        TestBase.base.id = "Juan"
        TestBase.base.number = 89
        TestBase.base.save()
        self.assertEqual(TestBase.base.__str__(),
                         f'[{TestBase.base.__class__.__name__}] '
                         f'({TestBase.base.id}) {TestBase.base.__dict__}')
