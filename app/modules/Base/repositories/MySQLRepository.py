import pymysql

from config import DB_CREDENTIALS


class MySQLRepository:

    _dbCredentials = DB_CREDENTIALS.copy()
    _dbCredentials['cursorclass'] = pymysql.cursors.DictCursor

    @classmethod
    def getConnection(cls):
        return pymysql.connect(**cls._dbCredentials)

    @property
    def connection(self):
        return MySQLRepository.getConnection()

    def fetchAll(self, query, args = ()):
        with self.connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(query, args)
                return cursor.fetchall()