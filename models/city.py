#!/usr/bin/python3
"""Import BaseModel."""
from models.base_model import BaseModel


class City(BaseModel):
    """City class."""

    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """Initialize with BaseModel."""
        BaseModel.__init__(self, *args, **kwargs)
