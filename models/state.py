#!/usr/bin/python3
"""Import BaseModel."""
from models.base_model import BaseModel


class State(BaseModel):
    """State class."""

    name = ""

    def __init__(self, *args, **kwargs):
        """Initialize with BaseModel."""
        BaseModel.__init__(self, *args, **kwargs)
