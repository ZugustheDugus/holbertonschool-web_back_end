#!/usr/bin/env python3
"""basic auth module None for now"""
from api.v1.auth.auth import Auth
from base64 import b64decode, binascii


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
        except binascii.Error:
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