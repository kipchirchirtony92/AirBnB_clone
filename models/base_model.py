from datetime import datetime
from uuid import uuid4


class BaseModel:
    """ represents the base model of the AirBnb project"""

    def __init__(self, *args, **kwargs):
        """initialization of the base model class
         Args:
             *args (any argument): unused
             **kwargs (dictionaty): key value pair of arguments
        """
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()

    def save(self):
        """updates the updated_at attribute to the current datetime"""
        self.updated_at = datetime.today()

    def to_dict(self):
        """ returns the dict rep of the Basemodel instance

        includes the __class__ attribute which rep the class name of the object
        """
        tmpdict = self.__dict__.copy()
        tmpdict["created_at"] = self.created_at.isoformat()
        tmpdict["updated_at"] = self.updated_at.isoformat()
        tmpdict["__class__"] = self.__class__.__name__
        return tmpdict

    def __str__(self):
        """ Returns the string rep of the Basemodel instance."""
        clsname = self.__class__.__name__
        return f"[{clsname}] ({self.id}) {self.__dict__}"
