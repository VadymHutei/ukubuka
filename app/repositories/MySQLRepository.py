import pymysql
from flask import current_app as app

from repositories.AbstractRepository import AbstractRepository


class MySQLRepository(AbstractRepository):

    def _get_connection(self):
        _db_credentials = app.config['MYSQL_DB_CREDENTIALS']
        _db_credentials['cursorclass'] = pymysql.cursors.DictCursor
        return pymysql.connect(**_db_credentials)

    @property
    def connection(self):
        return self._get_connection()