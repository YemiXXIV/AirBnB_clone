#!/usr/bin/python3
"""
Test Case Module for User Module

"""
import unittest
from datetime import datetime
from models.user import User


class TestUser(unittest.TestCase):
    """
    Test Class for Base Model
    """
    def test_no_arg(self):
        """Test instance creation with no arguments
        """
        tmp = User()
        no_list = []
        check_list = [
                'id', 'created_at',
                'updated_at', '__class__'
                ]
        for key in tmp.to_dict():
            no_list.append(key)
        self.assertEqual(no_list, check_list)

    def test_str(self):
        """
        Test instance creation with string
        """
        tmp_str = User()
        string_name = type(tmp_str).__name__
        string_id = tmp_str.id
        string_dict = str(tmp_str.__dict__)
        output = "[{}] ({}) {}".format(string_name, string_id, string_dict)
        self.assertEqual(str(tmp_str), output)

    def test_email_attribute(self):
        """
        Test class attributes
        """
        usr = User()
        self.assertEqual(usr.email, "")
        self.assertEqual(usr.password, "")
        self.assertEqual(usr.first_name, "")
        self.assertEqual(usr.last_name, "")


if __name__ == '__main__':
    unittest.main()
