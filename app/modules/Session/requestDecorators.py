from functools import wraps

from flask import current_app as app
from flask import g, make_response, request
from modules.Session.services.SessionService import SessionService
from modules.User.services.UserService import UserService


def with_session(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        session_service = SessionService()
        user_servive = UserService()
        response = make_response(f(*args, **kwargs))
        session_ID = request.cookies.get(app.config['SESSION_COOKIE_NAME'])

        g.session = session_service.get_session(session_ID)
        if g.session is None:
            g.session = session_service.start_session()
            response.set_cookie(
                app.config['SESSION_COOKIE_NAME'],
                value=g.session.ID,
                expires=g.session.expired_datetime,
                httponly=True,
            )

        g.user = user_servive.get_user_by_session_ID(g.session.ID)

        return response
    return decorated_function
