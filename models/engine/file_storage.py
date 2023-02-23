#!/usr/bin/python3
""" Module doc"""
import json
from os import path


class FileStorage:
    """ Class doc"""
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """ all doc"""
        return FileStorage.__objects

    def new(self, obj):
        """ new doc"""
        FileStorage.__objects[f'{obj.__class__.__name__}.{getattr(obj, "id")}'] = obj

    def save(self):
        """ save doc"""
        objs_dict = self.__objects
        objs_dump = {key: value.to_dict() for key, value in objs_dict.items()}
        with open(self.__file_path, mode='w', encoding='utf-8') as f:
            json.dump(objs_dump, f)

    def reload(self):
        """ reload doc"""
        from models.base_model import BaseModel
        if not path.exists(self.__file_path):
            return
        with open(self.__file_path, encoding='utf-8') as f:
            data = json.load(f)
            FileStorage.__objects = {}
            for key, value in data.items():
                self.__objects[key] = BaseModel(**value)
