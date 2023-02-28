#!/usr/bin/python3
""" Module doc"""
from models.base_model import BaseModel


class City(BaseModel):
    """ Class doc"""
    state_id = ""
    name = ""

    def __init__(self, args, **kwargs):
        BaseModel.__init__(self, args, **kwargs)
