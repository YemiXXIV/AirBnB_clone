#!/usr/bin/python3
"""
Test Case Module for User Module

"""
from unittest import TestCase
from models.user import User
from datetime import datetime


class TestUser(TestCase):
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

    def test_kwargs_args(self):
        """
        Tests instance creation with kwargs arguments
        """
        tmp_kwgs = User(name='Mustapha', age=24, time='now')
        no_list_kwgs = []
        check_list_kwgs = [
            'name', 'age', 'time', '__class__'
                ]
        for key in tmp_kwgs.to_dict():
            no_list_kwgs.append(key)
        self.assertEqual(no_list_kwgs, check_list_kwgs)

    def test_args_args(self):
        """
        Tests instance creation with args arguments
        """
        tmp_args = User(13, "new", "anything", 34.50)
        nolist_args = []
        check_list = [
                'id', 'created_at',
                'updated_at', '__class__'
                ]
        for key in tmp_args.to_dict():
            nolist_args.append(key)
        self.assertEqual(nolist_args, check_list)

    def test_args_and_kwargs(self):
        """
        Tests instance creation with args and kwargs
        """
        tmp_args_kwargs = User("every", "new", 23, name="Mustapha", age=20)
        list_ak = []
        check_list = [
            'name', 'age', '__class__'
                ]
        for key in tmp_args_kwargs.to_dict():
            list_ak.append(key)
        self.assertEqual(list_ak, check_list)

        
if __name__ == '__main__':
    unittest.main()
