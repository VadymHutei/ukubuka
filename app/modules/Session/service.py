from datetime import datetime, timedelta

from flask import request

from config import (PASSWORD_ABC,
    SESSION_ID_LENGTH, SESSION_LIFETIME_DAYS)
from vendor.Ukubuka.password import getSecret
from modules.Session.repository import SessionMySQLRepository


class SessionService:

    def __init__(self):
        self.repository = SessionMySQLRepository()

    def startSession(self):
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

    def getUserBySessionID(self, sessionID):
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