#!/usr/bin/python3
"""
Module containing the class Review
"""

from models.base_model import BaseModel


class Review(BaseModel):
    """Review representation"""

    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """Constructor of the class review"""
        super().__init__(*args, **kwargs)
