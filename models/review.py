#!/usr/bin/python3

"""
Module for review
"""

from models.base_model import BaseModel


class Review(BaseModel):
    """
    Defines the review object
    """
    place_id = ""
    user_id = ""
    text = ""
