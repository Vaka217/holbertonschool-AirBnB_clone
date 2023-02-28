#!/usr/bin/python3
"""Import BaseModel."""
from models.base_model import BaseModel


class User(BaseModel):
    """User class."""

    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """Initialize with BaseModel."""
        BaseModel.__init__(self, *args, **kwargs)
