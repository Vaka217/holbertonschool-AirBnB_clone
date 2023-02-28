#!/usr/bin/python3
""" Module doc"""
from models.base_model import BaseModel


class Review(BaseModel):
    """ Class doc"""
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, args, **kwargs):
        BaseModel.__init__(self, args, **kwargs)
