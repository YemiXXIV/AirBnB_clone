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
            with open(FileStorage.__file_path, 'r') as file:
                obj_dict = json.load(file)
                for key, value in obj_dict.items():
                    class_name = value['__class__']
                    module_name = 'models.base_model'
                    module = __import__(module_name, fromlist=[class_name])
                    class_obj = getattr(module, class_name)
                    FileStorage.__objects[key] = class_obj(**value)
