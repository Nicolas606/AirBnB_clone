#!/usr/bin/python3
"""Unit test for the module City"""

import unittest
from models.city import City
from models import storage


class TestingCity(unittest.TestCase):
    """ Testing for the class City """

    def testing_City_init(self):
        """ Testing for the method __init__ """
        obj = City()
        obj_name = 'City.' + obj.id
        new_dict = storage.all()
        class_City = "<class 'models.city.City'>"
        class_datetime = "<class 'datetime.datetime'>"

        self.assertEqual(str(type(obj)), class_City)
        self.assertEqual(str(type(obj.created_at)), class_datetime)
        self.assertEqual(str(type(obj.updated_at)), class_datetime)

        key = new_dict.get(obj_name).to_dict()
        self.assertIn(obj_name, new_dict.keys())
        self.assertIn("id", key.keys())
        self.assertIn("created_at", key.keys())
        self.assertIn("updated_at", key.keys())
        self.assertIn("name", key.keys())
        self.assertIn("state_id", key.keys())

        obj.name = "Bogota"
        obj.state_id = "Cundinamarca"
        self.assertIn("name", key.keys())
        self.assertIn("state_id", key.keys())
        self.assertEqual(key.get("name"), "Bogota")
        self.assertEqual(key.get("state_id"), "Cundinamarca")


    def testing_City_str(self):
        """ Testing for the method __str__ """
        obj = City()
        obj_string = '[City] ({}) {}'.format(obj.id, obj.__dict__)
        new_string = obj.__str__()
        self.assertEqual(obj_string, new_string)

    def testing_City_save(self):
        """ Testing for the method save """
        obj = City()
        obj_name = 'City.' + obj.id
        new_dict = storage.all()
        first_update = obj.updated_at
        obj.save()
        second_update = obj.updated_at
        self.assertIn(obj_name, new_dict.keys())
        self.assertNotEqual(first_update, second_update)

    def testing_City_to_dict(self):
        """ Testing for the method to_dict """
        obj = City()
        obj_name = 'City.' + obj.id
        new_dict = storage.all()
        self.assertIn(obj_name, new_dict.keys())


if __name__ == '__main__':
    unittest.main()
