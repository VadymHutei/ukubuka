from functools import wraps

from flask import request, make_response

from config import SESSION_COOKIE_NAME
from modules.Session.service import SessionService


def withSession(f):
    @wraps(f)
    def decoratedFunction(*args, **kwargs):
        sessionService = SessionService()

        sessionExpires = None
        sessionID = request.cookies.get(SESSION_COOKIE_NAME)
        if sessionID is None:
            sessionID, sessionExpires = sessionService.startSession()

        request.ctx['sessionID'] = sessionID
        request.ctx['user'] = sessionService.getUserBySessionID(sessionID)

        response = make_response(f(*args, **kwargs))
        if sessionExpires is not None:
            response.set_cookie(
                SESSION_COOKIE_NAME,
                value=request.ctx['sessionID'],
                expires=sessionExpires,
                httponly=True
            )
        return response
    return decoratedFunction