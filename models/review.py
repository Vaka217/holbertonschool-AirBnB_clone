#!/usr/bin/python3
"""Needed modules."""
from models.base_model import BaseModel


class Review(BaseModel):
    """Review class."""

    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """Initialize with BaseModel."""
        BaseModel.__init__(self, *args, **kwargs)
