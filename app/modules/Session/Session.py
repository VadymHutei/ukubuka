from modules.Session.service import SessionService


class Session:

    def __init__(self, sessionID):
        self.service = SessionService()
        self.id = sessionID
        self._userID = None

    def userID(self):
        if self._userID is None:
            self._userID = self.service.getUserIDBySessionID(self.id)