#!/usr/bin/python3

"""
Unittest for amenity.py
"""
import unittest
from models.engine.file_storage import FileStorage


class TestAmenity(unittest.TestCase):
    """
    Test case for Amenity class
    """
    def test_amenity_obj(self):
        """
        Test if Amenity object can be created
        """
        from models.amenity import Amenity
        obj = Amenity()
        self.assertEqual(obj.name, "")
