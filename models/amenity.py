#!/usr/bin/python3
"""Needed modules."""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Amenity class."""

    name = ""

    def __init__(self, *args, **kwargs):
        """Initialize with BaseModel."""
        BaseModel.__init__(self, *args, **kwargs)
