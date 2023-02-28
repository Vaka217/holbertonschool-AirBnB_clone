#!/usr/bin/python3
"""Needed modules."""
import uuid
from datetime import datetime
from models import storage


class BaseModel:
    """BaseModel class."""

    def __init__(self, *args, **kwargs):
        """Initialize class."""
        if kwargs:
            setattr(self, "created_at",
                    datetime.fromisoformat(kwargs["created_at"]))
            setattr(self, "updated_at",
                    datetime.fromisoformat(kwargs["updated_at"]))
            setattr(self, "id", kwargs["id"])
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """Modify str method."""
        return f'[{self.__class__.__name__}] ({self.id}) {self.__dict__}'

    def save(self):
        """Update update_at with current datetime."""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Return a dictionary containing all keys/values of __dict__ of the instance."""
        new_dict = self.__dict__.copy()
        new_dict.update({'__class__': self.__class__.__name__,
                         'created_at': self.created_at.isoformat(),
                         'updated_at': self.updated_at.isoformat()})
        return new_dict
