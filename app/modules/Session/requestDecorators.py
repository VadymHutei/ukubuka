from functools import wraps

from flask import current_app as app
from flask import g, make_response, request
from modules.Session.services.SessionService import SessionService


def with_session(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        session_service = SessionService()
        session_expires = None
        session_ID = request.cookies.get(app.config['SESSION_COOKIE_NAME'])

        if session_ID is None:
            session_ID, session_expires = session_service.start_session()

        g.session_ID = session_ID
        request.ctx['user'] = session_service.get_user_by_session_ID(session_ID)

        response = make_response(f(*args, **kwargs))
        if session_expires is not None:
            response.set_cookie(
                app.config['SESSION_COOKIE_NAME'],
                value=g.session_ID,
                expires=session_expires,
                httponly=True,
            )
        return response
    return decorated_function
