from datetime import datetime, timedelta
from typing import Optional

from flask import current_app as app
from flask import request
from modules.Auth.services.AuthService import AuthService
from modules.Session.entities.SessionEntity import SessionEntity
from modules.Session.repositories.SessionRepository import SessionRepository


class SessionService:

    def __init__(self):
        self._repository = SessionRepository()

    def get_session(self, session_ID: str) -> Optional[SessionEntity]:
        return self._repository.get_session(session_ID)

    def create_session(self) -> SessionEntity:
        session = SessionEntity(
            ID=AuthService.get_random_string(app.config['SESSION_ID_LENGTH'], app.config['PASSWORD_ABC']),
            created_datetime=datetime.now(),
            expired_datetime=datetime.now() + timedelta(days=app.config['SESSION_LIFETIME_DAYS']),
            user_agent=request.user_agent.string,
            is_new=True
        )

        self._repository.add_session(session)

        return session

    def getUserIDBySessionID(self, sessionID):
        if sessionID is None:
            return None
        result = self._repository.getUserIDBySessionID(sessionID)
        return None if result is None else int(result['user_id'])

    def get_user_by_session_ID(self, sessionID):
        if sessionID is None:
            return None
        return self._repository.getUserBySessionID(sessionID)

    def setSessionData(self, key, value, sessionID):
        if sessionID is None:
            return None
        self._repository.setSessionData(sessionID, key, value)

    def getSessionData(self, key, sessionID):
        if sessionID is None:
            return None
        result = self._repository.getSessionData(sessionID, key)
        return None if result is None else result['value']
