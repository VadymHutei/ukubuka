from flask import current_app as app
from pymysql import connect
from pymysql.cursors import DictCursor


class PyMySQLRepository:

    PLCHLD = '%'

    @property
    def connection(self):
        credentials = {'cursorclass': DictCursor}
        credentials.update(app.config['MYSQL_DB_CREDENTIALS'])

        return connect(**credentials)
