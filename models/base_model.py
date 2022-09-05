#!/usr/bin/python3
""" This module contains the BaseModel class """
import uuid
from datetime import datetime
import models


class BaseModel:
    """ This is the BaseModel class """
    def __init__(self, *args, **kwargs):
        """ This is the __init__ method """
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != "__class__":
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """ This is the __str__ method """
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id,
                                     self.__dict__)

    def save(self):
        """ This is the save method """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """ This is the to_dict method """
        new_dict = self.__dict__.copy()
        new_dict["__class__"] = self.__class__.__name__
        new_dict["created_at"] = self.created_at.isoformat()
        new_dict["updated_at"] = self.updated_at.isoformat()
        return new_dict

    def delete(self):
        """ This is the delete method """
        models.storage.delete(self)

