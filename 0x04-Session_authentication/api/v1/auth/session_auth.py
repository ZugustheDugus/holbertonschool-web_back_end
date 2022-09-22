#!/usr/bin/env python3
"""Module SessionAuth"""
from api.v1.auth.auth import Auth
from models.user import User
from uuid import uuid4


class SessionAuth(Auth):
    """Class SessionAuth inherits from Auth"""
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """Creates a session ID for user_id"""
        if user_id is None or type(user_id) is not str:
            return None
        ui = str(uuid4())
        SessionAuth.user_id_by_session_id[ui] = user_id
        return ui

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """returns user_id based on session id"""
        if session_id is None or type(session_id) is not str:
            return None
        return SessionAuth.user_id_by_session_id.get(session_id)

    def current_user(self, request=None):
        """returns User instance based on cookie value"""
        cookie_value = self.session_cookie(request)
        user = self.user_id_for_session_id(cookie_value)
        return User.get(user)

    def destroy_session(self, request=None):
        """logs out by deleting session"""
        if request is None:
            return False
        session_id = self.session_cookie(request)
        if session_id is None:
            return False
        u = self.user_id_for_session_id(session_id)
        if u is None:
            return False
        del self.user_id_by_session_id[session_id]
        return True
