import pymysql
from flask import current_app as app


class MySQLRepository:

    @classmethod
    def get_connection(cls):
        _db_credentials = app.config['MYSQL_DB_CREDENTIALS']
        _db_credentials['cursorclass'] = pymysql.cursors.DictCursor
        return pymysql.connect(**_db_credentials)

    @property
    def connection(self):
        return MySQLRepository.get_connection()

    def fetchAll(self, query, args=()):
        with self.connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(query, args)
                return cursor.fetchall()
