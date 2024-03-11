#!/usr/bin/python3
"""
Test Case Module for User Module

"""
from unittest import TestCase
from models.user import User
from datetime import datetime
from models import storage
from models.base_model import BaseModel


class TestUser(TestCase):
    """
    Test Class for Base Model
    """
    @classmethod
    def setUpClass(cls):
        """Setup the unittest"""
        cls.user = User()
        cls.user.email = "mustapha.yinusa@gmail.com"
        cls.user.password = "1946"
        cls.user.first_name = "Mustapha"
        cls.user.last_name = "Yinusa"

    def test_for_instantiation(self):
        """Tests instantiation of User class."""
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

        
if __name__ == "__main__":
    unittest.main()
