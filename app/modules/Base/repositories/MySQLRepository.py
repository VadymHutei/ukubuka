import pymysql
from flask import current_app as app


class MySQLRepository:

    @classmethod
    def getConnection(cls):
        _dbCredentials = app.config['DB_CREDENTIALS']
        _dbCredentials['cursorclass'] = pymysql.cursors.DictCursor
        return pymysql.connect(**_dbCredentials)

    @property
    def connection(self):
        return MySQLRepository.getConnection()

    def fetchAll(self, query, args = ()):
        with self.connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(query, args)
                return cursor.fetchall()