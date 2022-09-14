#!/usr/bin/env python3
"""Password encryption functions which use bcrypt
"""


import bcrypt


def hash_password(password: str) -> bytes:
    """ Function that expects a string argument named
    'password' which returns a salted, hashed password,
    which is a byte string """
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())


def is_valid(hashed_password: bytes, password: str) -> bool:
    """ Implements an 'is_valid' function that expects 2 arguments and
    returns a boolean """
    return bcrypt.checkpw(password.encode(), hashed_password)
