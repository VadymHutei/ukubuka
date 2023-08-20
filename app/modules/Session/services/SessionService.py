from datetime import datetime, timedelta

from flask import current_app as app
from flask import request

from modules.Auth.services.AuthService import AuthService
from modules.Session.entities.SessionEntity import SessionEntity
from modules.Session.repositories.SessionMySQLRepository import SessionMySQLRepository
from modules.Session.repositories.SessionRedisRepository import SessionRedisRepository


class SessionService:

    def __init__(self):
        self._MySQL_repository = SessionMySQLRepository()
        self._Redis_repository = SessionRedisRepository()

    def get_session(self, session_ID: str) -> SessionEntity|None:
        return self._Redis_repository.get_session(session_ID)

    def create_session(self) -> SessionEntity:
        session = SessionEntity(
            ID=AuthService.get_random_string(app.config['SESSION_ID_LENGTH'], app.config['PASSWORD_ABC']),
            created_datetime=datetime.now(),
            last_visit_datetime=datetime.now(),
            expired_datetime=datetime.now() + timedelta(days=app.config['SESSION_LIFETIME_DAYS']),
            user_agent=request.user_agent.string,
        )

        self._Redis_repository.set_session(session)

        return session

    def getUserIDBySessionID(self, sessionID):
        if sessionID is None:
            return None
        result = self._MySQL_repository.getUserIDBySessionID(sessionID)
        return None if result is None else int(result['user_id'])

    def get_user_by_session_ID(self, sessionID):
        if sessionID is None:
            return None
        return self._MySQL_repository.getUserBySessionID(sessionID)

    def setSessionData(self, key, value, sessionID):
        if sessionID is None:
            return None
        self._MySQL_repository.setSessionData(sessionID, key, value)

    def getSessionData(self, key, sessionID):
        if sessionID is None:
            return None
        result = self._MySQL_repository.getSessionData(sessionID, key)
        return None if result is None else result['value']

    def update_last_visit(self, session: SessionEntity):
        session.last_visit_datetime = datetime.now()
        session.expired_datetime = datetime.now() + timedelta(days=app.config['SESSION_LIFETIME_DAYS'])
        session.user_agent = request.user_agent.string

        self._Redis_repository.set_session(session)
