#!/usr/bin/env python3
"""basic auth module None for now"""
from api.v1.auth.auth import Auth
from base64 import b64decode, binascii
from typing import TypeVar


class BasicAuth(Auth):
    """BasicAuth Class that is None for now"""

    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """ return Base64 part of auth_header """
        if authorization_header is None:
            return None
        if type(authorization_header) is not str:
            return None
        if "Basic " in authorization_header:
            return authorization_header[6:]
        return None

    def decode_base64_authorization_header(self,
                                           base64_authorization_header:
                                           str) -> str:
        """ decodes base64 """
        if base64_authorization_header is None:
            return None
        if type(base64_authorization_header) is not str:
            return None
        try:
            return b64decode(base64_authorization_header).decode('utf-8')
        except Exception:
            return None

    def extract_user_credentials(self,
                                 decoded_base64_authorization_header:
                                 str) -> (str, str):
        """Extracts user information"""
        if decoded_base64_authorization_header is None:
            return (None, None)
        if type(decoded_base64_authorization_header) is not str:
            return (None, None)
        if ":" not in decoded_base64_authorization_header:
            return (None, None)
        dec = decoded_base64_authorization_header.split(':')
        tup_dec = (dec[0], dec[1])
        return tup_dec

    def user_object_from_credentials(self,
                                     user_email: str,
                                     user_pwd: str) -> TypeVar('User'):
        """returns User object based on email and password"""
        from models.user import User
        if user_email is None or type(user_email) is not str:
            return None
        if user_pwd is None or type(user_pwd) is not str:
            return None
        d = {'email': user_email}
        try:
            u = User.search(d)
            if u is not None or u != []:
                if u[0].is_valid_password(user_pwd):
                    return u[0]
        except Exception:
            return None

    def current_user(self, request=None) -> TypeVar('User'):
        """overloads Auth and retrieves User"""
        header = self.authorization_header(request)
        b64 = self.extract_base64_authorization_header(header)
        db64 = self.decode_base64_authorization_header(b64)
        user_cred = self.extract_user_credentials(db64)
        return self.user_object_from_credentials(user_cred[0], user_cred[1])
