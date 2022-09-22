#!/usr/bin/env python3
""" holds auth class """
from flask import request
from typing import TypeVar, List
import os
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
        """Implement later in BasicAuth"""
        return None

    def session_cookie(self, request=None):
        """Returns the session cookie value of request"""
        if request is None:
            return None
        session_name = os.getenv('SESSION_NAME')
        cookies = request.headers.get('Cookie')
        if cookies is not None:
            cookies = cookies.split("=")
            if cookies[0] == session_name:
                return cookies[1]
