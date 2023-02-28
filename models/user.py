#!/usr/bin/python3
""" Module doc"""
from models.base_model import BaseModel


class User(BaseModel):
    """ Class doc"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, args, **kwargs):
        BaseModel.__init__(self, args, **kwargs)
