import pymysql

from config import DB_CREDENTIALS


class Repository:

    def __init__(self):
        self._dbCredentials = DB_CREDENTIALS.copy()
        self._dbCredentials['cursorclass'] = pymysql.cursors.DictCursor

    def getConnection(self):
        return pymysql.connect(**self._dbCredentials)