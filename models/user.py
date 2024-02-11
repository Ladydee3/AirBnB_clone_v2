#!/usr/bin/python3
"""This module creates a User class"""
from modules.base_model import BaseModel


class User(BaseModel):
    """Class for managing user objects"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
