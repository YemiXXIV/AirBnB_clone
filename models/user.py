#!/usr/bin/python3
"""
User Module
"""

from models.base_model import BaseModel


class User(BaseModel):
    """Class for User
    Arguments:
        email (str)
        password (str)
        first_name (str)
        last_name (str)
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
