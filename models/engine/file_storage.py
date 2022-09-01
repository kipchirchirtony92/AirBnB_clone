#!/usr/bin/python3
"""Defines the file storage file"""
import json
from models.base_model import BaseModel


class FileStorage:
    """ represents an abstract of the storage engine
    Attributes:
              __file_path(str):the file where instansiated objects are stored
              __objects(dict): a dictionary of the instantiated objects
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ returns the dictionary of all __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        obj_cls_name = obj.__class__.__name__
        FileStorage.__objects[f"{obj_cls_name}.{obj.id}"] = obj

    def save(self):
        """ serializes __objects to the JSON file (__file_path)"""
        with open(FileStorage.__file_path, 'w') as f:
            json.dump({k: v.to_dict()
                       for k, v in FileStorage.__objects.items()}, f)

    def reload(self):
        """Deserialize the JSON file __file_path to __objects, if it exists."""
        try:
            with open(FileStorage.__file_path, 'r') as f:
                objdict = json.load(f)
                for value in objdict.values():
                    cls = value["__class__"]
                    self.new(eval(cls)(**value))
        except FileNotFoundError:
            return
