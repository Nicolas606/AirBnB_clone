#!/usr/bin/python3
"""Unit test for the class base_model"""

import unittest
from models.base_model import BaseModel
from models import storage


class TestingBaseModel(unittest.TestCase):
    """ Testing for the BaseModel """

    def testing_init(self):
        """ Testing for the method __init__ """
        obj = BaseModel()
        obj_name = 'BaseModel.' + obj.id
        new_dict = storage.all()
        class_BaseModel = "<class 'models.base_model.BaseModel'>"
        class_datetime = "<class 'datetime.datetime'>"

        self.assertEqual(str(type(obj)), class_BaseModel)
        self.assertEqual(str(type(obj.created_at)), class_datetime)
        self.assertEqual(str(type(obj.updated_at)), class_datetime)

        key = new_dict.get(obj_name).to_dict()
        self.assertIn(obj_name, new_dict.keys())
        self.assertIn("id", key.keys())
        self.assertIn("created_at", key.keys())
        self.assertIn("updated_at", key.keys())

        obj.name = "Holberton"
        obj.last_name = "Cheker"
        obj.my_number = 89
        self.assertIn("name", key.keys())
        self.assertIn("last_name", key.keys())
        self.assertIn("my_number", key.keys())
        self.assertEqual(key.get("name"), "Holberton")
        self.assertEqual(key.get("last_name"), "Cheker")
        self.assertEqual(key.get("my_number"), 89)

    def testing_str(self):
        """ Testing for the method __str__ """
        obj = BaseModel()
        obj_string = '[BaseModel] ({}) {}'.format(obj.id, obj.__dict__)
        new_string = obj.__str__()
        self.assertEqual(obj_string, new_string)

    def testing_save(self):
        """ Testing for the method save """
        obj = BaseModel()
        obj_name = 'BaseModel.' + obj.id
        new_dict = storage.all()
        first_update = obj.updated_at
        obj.save()
        second_update = obj.updated_at
        self.assertIn(obj_name, new_dict.keys())
        self.assertNotEqual(first_update, second_update)

    def testing_to_dict(self):
        """ Testing for the method to_dict """
        obj = BaseModel()
        obj_name = 'BaseModel.' + obj.id
        new_dict = storage.all()
        self.assertIn(obj_name, new_dict.keys())


if __name__ == '__main__':
    unittest.main()
