#!/usr/bin/python3

"""

This module defines a class that serializes and deserializes
JSON data

"""
import json
from os import path


class FileStorage:
    """
    Methods for JSON data serialization and deserialization
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Returns the dictionary of objects
        """
        return (FileStorage.__objects)

    def new(self, obj):
        """
        Adds an object to the dictionary
        """
        classname_id = obj.__class__.__name__ + "." + obj.id
        FileStorage.__objects[classname_id] = obj

    def save(self):
        """
        Saves objects to the dictionary
        """
        obj_dict = {}
        for key, obj in FileStorage.__objects.items():
            obj_dict[key] = obj.to_dict()
            with open(FileStorage.__file_path, 'w') as file:
                json.dump(obj_dict, file)

    def reload(self):
        """
        Reload dictionary of objects from a file
        """
        if path.isfile(FileStorage.__file_path):
            obj_dict = {}
            with open(FileStorage.__file_path, 'r') as file:
                obj_dict = json.loads(file.read())
            from models.base_model import BaseModel
            from models.user import User
            from models.amenity import Amenity
            from models.review import Review
            from models.city import City
            from models.place import Place
            from models.state import State
            for key, value in obj_dict.items():
                class_name = value["__class__"]
                del value["__class__"]
                FileStorage.__objects[key] = eval(class_name + "(**value)")
