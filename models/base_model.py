#!/usr/bin/python3
""" Module doc"""
import uuid
from datetime import datetime
from models import storage


class BaseModel:
    """ Class doc"""
    def __init__(self, *args, **kwargs):
        """ __init__ doc"""
        if kwargs:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    setattr(self, key, datetime.fromisoformat(value))
                elif key != '__class__':
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """ __str__ doc"""
        return f'[{self.__class__.__name__}] ({self.id}) {self.__dict__}'

    def save(self):
        """ save doc"""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """ to_dict doc"""
        new_dict = self.__dict__.copy()
        new_dict['__class__'] = self.__class__.__name__
        new_dict['created_at']= self.created_at.isoformat()
        new_dict['updated_at']= self.updated_at.isoformat()
        return new_dict
