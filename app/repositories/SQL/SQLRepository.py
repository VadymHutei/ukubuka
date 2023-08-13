from pymysql import connect
from pymysql.cursors import DictCursor
from flask import current_app as app


class SQLRepository:

    _TABLE: str

    def _get_connection(self):
        credentials = {"cursorclass": DictCursor}
        credentials.update(app.config['MYSQL_DB_CREDENTIALS'])
        return connect(**credentials)

    @property
    def connection(self):
        return self._get_connection()

    @classmethod
    def get_text_table(self):
        return f'{self._TABLE}_text'