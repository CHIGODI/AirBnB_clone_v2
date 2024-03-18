#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel


class User(BaseModel):
    """This class defines a user by various attributes"""
    email = ''
    password = ''
    first_name = ''
    last_name = ''

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        User.email = kwargs.get('email', User.email)
        User.password = kwargs.get('password', User.password)
        User.first_name = kwargs.get('first_name', User.first_name)
        User.last_name = kwargs.get('last_name', User.last_name)
