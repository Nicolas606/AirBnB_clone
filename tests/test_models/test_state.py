#!/usr/bin/python3
"""Unit test for the module State"""

import unittest
from models.state import State
from models import storage


class TestingState(unittest.TestCase):
    """ Testing for the class State """

    def testing_State_init(self):
        """ Testing for the method __init__ """
        obj = State()
        obj_name = 'State.' + obj.id
        new_dict = storage.all()
        class_State = "<class 'models.state.State'>"
        class_datetime = "<class 'datetime.datetime'>"

        self.assertEqual(str(type(obj)), class_State)
        self.assertEqual(str(type(obj.created_at)), class_datetime)
        self.assertEqual(str(type(obj.updated_at)), class_datetime)

        key = new_dict.get(obj_name).to_dict()
        self.assertIn(obj_name, new_dict.keys())
        self.assertIn("id", key.keys())
        self.assertIn("created_at", key.keys())
        self.assertIn("updated_at", key.keys())
        self.assertIn("name", key.keys())

        obj.name = "Bogota"
        self.assertIn("name", key.keys())
        self.assertEqual(key.get("name"), "Bogota")

    def testing_State_str(self):
        """ Testing for the method __str__ """
        obj = State()
        obj_string = '[State] ({}) {}'.format(obj.id, obj.__dict__)
        new_string = obj.__str__()
        self.assertEqual(obj_string, new_string)

    def testing_State_save(self):
        """ Testing for the method save """
        obj = State()
        obj_name = 'State.' + obj.id
        new_dict = storage.all()
        first_update = obj.updated_at
        obj.save()
        second_update = obj.updated_at
        self.assertIn(obj_name, new_dict.keys())
        self.assertNotEqual(first_update, second_update)

    def testing_State_to_dict(self):
        """ Testing for the method to_dict """
        obj = State()
        obj_name = 'State.' + obj.id
        new_dict = storage.all()
        self.assertIn(obj_name, new_dict.keys())


if __name__ == '__main__':
    unittest.main()
