#!/usr/bin/python3
""" Module doc"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """ Class doc"""
    name = ""

    def __init__(self, args, **kwargs):
        BaseModel.__init__(self, args, **kwargs)
