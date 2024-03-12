#!/usr/bin/python3

"""

BaseModel module that defines all common methods
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
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            for arg in kwargs:
                if arg == "created_at":
                    val = datetime.strptime(kwargs[arg],
                                            '%Y-%m-%dT%H:%M:%S.%f')
                    self.created_at = val
                elif arg == "updated_at":
                    val = datetime.strptime(kwargs[arg],
                                            '%Y-%m-%dT%H:%M:%S.%f')
                    self.updated_at = val
                elif arg != "__class__":
                    setattr(self, arg, kwargs[arg])
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
        obj_dictionary = {
            key: value if key != 'created_at' and key !=
            'updated_at' else value.isoformat()
            for key, value in self.__dict__.items()
        }
        obj_dictionary["__class__"] = type(self).__name__
        return obj_dictionary
