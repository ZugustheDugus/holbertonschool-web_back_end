#!/usr/bin/env python3
""" holds auth class """
from flask import request
from typing import TypeVar, List
import re


class Auth:
    """ Auth class that includes auth methods"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ checks the current list of paths """
        if excluded_paths is None or path is None:
            return True
        for p in excluded_paths:
            path_regex = re.compile(f'{p[:-1]}/?')
            if path_regex.search(path):
                return False
        return True

    def authorization_header(self, request=None) -> str:
        """checks for Authorization header key"""
        if request is None:
            return None
        if 'Authorization' in request.headers:
            return request.headers['Authorization']
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """Implement later and is empty for now"""
        return None