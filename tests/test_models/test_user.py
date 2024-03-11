#!/usr/bin/python3
"""
Test Case Module for User Module

"""
import unittest
from models.user import User
from datetime import datetime
from models import storage
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    """
    Test Class for Base Model
    """
    @classmethod
    def setUpClass(cls):
        """
        Setup the unittest
        """
        cls.user = User()
        cls.user.email = "mustapha.yinusa@gmail.com"
        cls.user.password = "1946"
        cls.user.first_name = "Mustapha"
        cls.user.last_name = "Yinusa"

    def test_for_instantiation(self):
        """
        Tests instantiation of User class.
        """
        user = User()
        self.assertEqual(str(type(user)), "<class 'models.user.User'>")
        self.assertIsInstance(user, User)
        self.assertTrue(issubclass(type(user), BaseModel))

    def test_type(self):
        self.assertEqual(type(User()), User)

    def test_new_instance_stored_in_objects(self):
        self.assertIn(User(), storage.all().values())

    def test_attrs(self):
        self.assertTrue('id' in self.user.__dict__)
        self.assertTrue('email' in self.user.__dict__)
        self.assertTrue('first_name' in self.user.__dict__)
        self.assertTrue('last_name' in self.user.__dict__)
        self.assertTrue('password' in self.user.__dict__)
        self.assertTrue('created_at' in self.user.__dict__)
        self.assertTrue('updated_at' in self.user.__dict__)

    def test_to_dict(self):
        self.assertTrue('to_dict' in dir(self.user))

    def test_save(self):
        self.user.save()
        self.assertNotEqual(self.user.created_at, self.user.updated_at)

    def test_to_dict_creates_dict(self):
        """
        test to_dict method creates a dictionary with proper attrs
        """
        u = User()
        new_d = u.to_dict()
        self.assertEqual(type(new_d), dict)
        for attr in u.__dict__:
            self.assertTrue(attr in new_d)
            self.assertTrue("__class__" in new_d)


if __name__ == "__main__":
    unittest.main()
