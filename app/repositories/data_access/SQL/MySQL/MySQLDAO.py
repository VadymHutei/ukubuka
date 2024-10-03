from flask import current_app as app
from pymysql import connect
from pymysql.cursors import DictCursor

from repositories.data_access.DAO import DAO


class MySQLDAO(DAO):

    @property
    def _connection(self):
        credentials = {'cursorclass': DictCursor}
        credentials.update(app.config['MYSQL_DB_CREDENTIALS'])

        return connect(**credentials)
