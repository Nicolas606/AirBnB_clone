#!/usr/bin/python3
"""
Module containing the class User
"""

from models.base_model import BaseModel

class User(BaseModel):
    """User representation"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """Constructor of the calss user"""
        super().__init__(*args, **kwargs)
