from datetime import datetime, timedelta

from config import PASSWORD_ABC, SESSION_ID_LENGTH, SESSION_LIFETIME_DAYS
from flask import request
from modules.Session.repository import SessionMySQLRepository
from vendor.ukubuka.password import getSecret


class SessionService:

    def __init__(self):
        self.repository = SessionMySQLRepository()

    def start_session(self):
        sessionID = getSecret(PASSWORD_ABC, SESSION_ID_LENGTH)
        currentDatetime = datetime.now()
        sessionExpires = currentDatetime + timedelta(days=SESSION_LIFETIME_DAYS)
        user_agent = request.user_agent.string
        self.repository.addSession(sessionID, currentDatetime, sessionExpires, user_agent)
        return sessionID, sessionExpires

    def getUserIDBySessionID(self, sessionID):
        if sessionID is None:
            return None
        result = self.repository.getUserIDBySessionID(sessionID)
        return None if result is None else int(result['user_id'])

    def get_user_by_session_ID(self, sessionID):
        if sessionID is None:
            return None
        return self.repository.getUserBySessionID(sessionID)

    def setSessionData(self, key, value, sessionID):
        if sessionID is None:
            return None
        self.repository.setSessionData(sessionID, key, value)

    def getSessionData(self, key, sessionID):
        if sessionID is None:
            return None
        result = self.repository.getSessionData(sessionID, key)
        return None if result is None else result['value']
