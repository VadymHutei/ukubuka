from datetime import datetime
from functools import wraps

from flask import current_app as app
from flask import g, make_response, request

from modules.Session.services.SessionService import SessionService


def with_session(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        session_service = SessionService()

        is_new_session = False

        session_id = request.cookies.get(app.config['SESSION_COOKIE_NAME'])

        if session_id is None:
            g.session = session_service.create_session()
            is_new_session = True
        else:
            g.session = session_service.get_session(session_id)
            if g.session is None or g.session.expired_datetime < datetime.now():
                g.session = session_service.create_session()
                is_new_session = True

        if not is_new_session:
            session_service.update_last_visit(g.session)

        response = make_response(f(*args, **kwargs))
        response.set_cookie(
            app.config['SESSION_COOKIE_NAME'],
            value=g.session.ID,
            expires=g.session.expired_datetime,
            httponly=True,
        )

        return response

    return decorated_function
