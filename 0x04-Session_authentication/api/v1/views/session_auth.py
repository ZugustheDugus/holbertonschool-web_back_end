#!/usr/bin/env python3
""" Module of session_auth views
"""
from flask import jsonify, abort, request
from api.v1.views import app_views
from models.user import User
import os


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def auth_session_login() -> str:
    """ POST /api/v1/auth_session/login
    Return:
      - User instance
    """
    from api.v1.app import auth
    email = request.form.get('email')
    pwd = request.form.get('password')
    if email is None or email == "":
        return jsonify({"error": "email missing"}), 400
    if pwd is None or pwd == "":
        return jsonify({"error": "password missing"}), 400
    d = {'email': email}
    try:
        u = User.search(d)
        if u is None or u == []:
            return jsonify({"error": "no user found for this email"}), 404
    except Exception:
        return jsonify({"error": "no user found for this email"}), 404
    if not u[0].is_valid_password(pwd):
        return jsonify({"error": "wrong password"}), 401
    sid = auth.create_session(u[0].id)
    out = jsonify(u[0].to_json())
    out.set_cookie(os.getenv('SESSION_NAME'), sid)
    return out


@app_views.route('/auth_session/logout',
                 methods=['DELETE'],
                 strict_slashes=False)
def auth_session_logout() -> str:
    """ DELETE /api/v1/auth_session/login
    Return:
      - User instance
    """
    from api.v1.app import auth
    if not auth.destroy_session(request):
        abort(404)
    return jsonify({}), 200
