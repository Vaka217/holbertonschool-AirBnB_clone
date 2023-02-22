#!/usr/bin/python3
""" Module doc"""
import json
from os import path
from datetime import datetime


class FileStorage:
    """ Class doc"""
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """ all doc"""
        return FileStorage.__objects

    def new(self, obj):
        """ new doc"""
        FileStorage.__objects[f'{obj.__class__.__name__}.{getattr(obj, "id")}'] = obj.__dict__

    def save(self):
        """ save doc"""
        with open(FileStorage.__file_path, mode='w', encoding='utf-8') as f:
            json.dump(FileStorage.__objects, f, default=str)

    def reload(self):
        """ reload doc"""
        from models.base_model import BaseModel
        if not path.exists(FileStorage.__file_path):
            return
        try:
            with open(FileStorage.__file_path, encoding='utf-8') as f:
                data = json.load(f)
            for key, value in data.items():
                data[key] = BaseModel(**value)
            FileStorage.__objects = data
        except json.decoder.JSONDecodeError:
            FileStorage.__objects = {}
