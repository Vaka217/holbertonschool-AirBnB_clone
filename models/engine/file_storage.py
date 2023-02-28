#!/usr/bin/python3
"""Needed modules."""
import json
from os import path


class FileStorage:
    """FileStorage class."""

    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """Return the dictionary __objects."""
        return FileStorage.__objects

    def new(self, obj):
        """Set in __objects the obj with key."""
        FileStorage.__objects[f'{obj.__class__.__name__}.'
                              f'{getattr(obj, "id")}'] = obj

    def save(self):
        """Serialize __objects to the JSON file."""
        objs_dict = self.__objects
        objs_dump = {key: value.to_dict() for key, value in objs_dict.items()}
        with open(self.__file_path, mode='w', encoding='utf-8') as f:
            json.dump(objs_dump, f)

    def reload(self):
        """Deserialize the JSON file to __objects."""
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review

        if not path.exists(self.__file_path):
            return
        classes = {'BaseModel': BaseModel, 'User': User, 'State': State,
                   'City': City, 'Amenity': Amenity, 'Place': Place,
                   'Review': Review}
        with open(self.__file_path, encoding='utf-8') as f:
            data = json.load(f)
            FileStorage.__objects = {}
            for key, value in data.items():
                other_key = key.split(".")[0]
                self.__objects[key] = classes[other_key](**value)
