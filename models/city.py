#!/usr/bin/python3
"""
Module containing the class City
"""

from models.base_model import BaseModel

class City(BaseModel):
    """City representation"""

    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """Constructor of the class city"""
        super().__init__(*args, **kwargs)
