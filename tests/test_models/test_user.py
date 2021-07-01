#!/usr/bin/python3
"""Unit test for the module User"""

import unittest
from models.user import User
from models import storage


class TestingUser(unittest.TestCase):
    """ Testing for the class User """

    def testing_User_init(self):
        """ Testing for the method __init__ """
        obj = User()
        obj_name = 'User.' + obj.id
        new_dict = storage.all()
        class_User = "<class 'models.user.User'>"
        class_datetime = "<class 'datetime.datetime'>"

        self.assertEqual(str(type(obj)), class_User)
        self.assertEqual(str(type(obj.created_at)), class_datetime)
        self.assertEqual(str(type(obj.updated_at)), class_datetime)

        key = new_dict.get(obj_name).to_dict()
        self.assertIn(obj_name, new_dict.keys())
        self.assertIn("id", key.keys())
        self.assertIn("created_at", key.keys())
        self.assertIn("updated_at", key.keys())
        self.assertIn("email", key.keys())
        self.assertIn("password", key.keys())
        self.assertIn("First_name", key.keys())
        self.assertIn("Last_name", key.keys())

        obj.email = "airbnb@holbertonshool.com"
        obj.password = "root"
        obj.first_name = "Betty"
        obj.last_name = "Holberton"
        self.assertEqual(key.get("email"), "airbnb@holbertonshool.com")
        self.assertEqual(key.get("password"), "root")
        self.assertEqual(key.get("first_name"), "Betty")
        self.assertEqual(key.get("last_name"), "Holberton")

    def testing_User_str(self):
        """ Testing for the method __str__ """
        obj = User()
        obj_string = '[User] ({}) {}'.format(obj.id, obj.__dict__)
        new_string = obj.__str__()
        self.assertEqual(obj_string, new_string)

    def testing_User_save(self):
        """ Testing for the method save """
        obj = User()
        obj_name = 'User.' + obj.id
        new_dict = storage.all()
        first_update = obj.updated_at
        obj.save()
        second_update = obj.updated_at
        self.assertIn(obj_name, new_dict.keys())
        self.assertNotEqual(first_update, second_update)

    def testing_User_to_dict(self):
        """ Testing for the method to_dict """
        obj = User()
        obj_name = 'User.' + obj.id
        new_dict = storage.all()
        self.assertIn(obj_name, new_dict.keys())


if __name__ == '__main__':
    unittest.main()
