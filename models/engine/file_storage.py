#!/usr/bin/python3

"""

This module defines a class that serializes and deserializes
JSON data

"""
import json
from os import path


class FileStorage():
    """
    Methods for data serialization, deserialization and storage
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Gets the dictionary of objects
        """
        return (FileStorage.__objects)

    def new(self, obj):
        """
        Add an object to a dictionary
        """
        classname_id = type(obj).__name__ + "." + str(obj.id)
        FileStorage.__objects[classname_id] = obj

    def save(self):
        """
        Saves dict of objects to a file
        """
        obj_dict = {}
        for key, value in FileStorage.__objects.items():
            obj_dict[key] = value.to_dict()
        with open(FileStorage.__file_path, "w") as file:
            file.write(json.dumps(obj_dict))

    def reload(self):
        """
        Reloads the dict of objects from a file
        """
        if path.isfile(FileStorage.__file_path):
            obj_dict = {}
            with open(FileStorage.__file_path, "r") as file:
                obj_dict = json.loads(file.read())
            from models.base_model import BaseModel
            from models.user import User
            from models.state import State
            from models.amenity import Amenity
            from models.place import Place
            from models.city import City
            from models.review import Review
            for key, value in obj_dict.items():
                class_name = value["__class__"]
                del value["__class__"]
                FileStorage.__objects[key] = eval(class_name + "(**value)")
