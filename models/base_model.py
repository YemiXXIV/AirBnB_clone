#!/usr/bin/python3

"""
BaseModel module that defines all common attributes/methods
for the AirBnb clone project
"""
import uuid
from datetime import datetime
from models import storage


class BaseModel:
    """
    BaseModel class that defines all common attributes/methods
    """
    def __init__(self, *args, **kwargs):
        """
        Initializes when an instance of BaseModel is called
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    setattr(self, key, datetime.strptime(
                        value, '%Y-%m-%dT%H:%M:%S.%f'))
                elif key != '__class__':
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """
        Return string representation of basemodel instance
        """
        string_name = type(self).__name__
        string_id = self.id
        string_dict = str(self.__dict__)
        return "[{}] ({}) {}".format(string_name, string_id, string_dict)

    def save(self):
        """
        Updates the updated_at attribute with current datetime and
        persists it
        """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """
        Returns the dict representation of the object to be
        serializable with JSON
        """
        obj_dict = self.__dict__.copy()
        obj_dict["__class__"] = type(self).__name__
        obj_dict["created_at"] = self.created_at.isoformat()
        obj_dict["updated_at"] = self.updated_at.isoformat()
        return obj_dict
