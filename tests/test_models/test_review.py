#!/usr/bin/python3
"""Unit test for the module Review"""

import unittest
from models.review import Review
from models import storage


class TestingReview(unittest.TestCase):
    """ Testing for the class Review """

    def testing_Review_init(self):
        """ Testing for the method __init__ """
        obj = Review()
        obj_name = 'Review.' + obj.id
        new_dict = storage.all()
        class_Review = "<class 'models.review.Review'>"
        class_datetime = "<class 'datetime.datetime'>"

        self.assertEqual(str(type(obj)), class_Review)
        self.assertEqual(str(type(obj.created_at)), class_datetime)
        self.assertEqual(str(type(obj.updated_at)), class_datetime)

        key = new_dict.get(obj_name).to_dict()
        self.assertIn(obj_name, new_dict.keys())
        self.assertIn("id", key.keys())
        self.assertIn("created_at", key.keys())
        self.assertIn("updated_at", key.keys())
        self.assertIn("place_id", key.keys())
        self.assertIn("user_id", key.keys())
        self.assertIn("text", key.keys())

        obj.place_id = ""
        obj.user_id = ""
        obj.text = ""
        self.assertEqual(key.get("place_id"), "")
        self.assertEqual(key.get("user_id"), "")
        self.assertEqual(key.get("text"), "")

    def testing_Review_str(self):
        """ Testing for the method __str__ """
        obj = Review()
        obj_string = '[Review] ({}) {}'.format(obj.id, obj.__dict__)
        new_string = obj.__str__()
        self.assertEqual(obj_string, new_string)

    def testing_Review_save(self):
        """ Testing for the method save """
        obj = Review()
        obj_name = 'Review.' + obj.id
        new_dict = storage.all()
        first_update = obj.updated_at
        obj.save()
        second_update = obj.updated_at
        self.assertIn(obj_name, new_dict.keys())
        self.assertNotEqual(first_update, second_update)

    def testing_Review_to_dict(self):
        """ Testing for the method to_dict """
        obj = Review()
        obj_name = 'Review.' + obj.id
        new_dict = storage.all()
        self.assertIn(obj_name, new_dict.keys())


if __name__ == '__main__':
    unittest.main()
