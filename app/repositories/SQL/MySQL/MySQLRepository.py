from typing import Type

from flask import current_app as app
from pymysql import connect
from pymysql.cursors import DictCursor

from entities.Entity import Entity
from entity_mappers.SQL.MySQL.MySQLEntityMapper import MySQLEntityMapper
from repositories.SQL.SQLRepository import SQLRepository


def _get_connection():
    credentials = {'cursorclass': DictCursor}

    credentials.update(app.config['MYSQL_DB_CREDENTIALS'])

    return connect(**credentials)


class MySQLRepository(SQLRepository):

    mapper: Type[MySQLEntityMapper] | None
    text_mapper: Type[MySQLEntityMapper] | None

    @property
    def connection(self):
        return _get_connection()

    def update(self, entity: Entity) -> bool:
        set_fields_statement, set_field_values = self.mapper.get_set_data(entity)

        query = f'''
            UPDATE {self.mapper.table}
            SET {set_fields_statement}
            WHERE id = %s
        '''

        query_data = (*set_field_values, entity.id,)

        with self.connection as connection:
            with connection.cursor() as cursor:
                result = cursor.execute(query, query_data) > 0

            connection.commit()

        return result

    def delete_by_code(self, code: str) -> bool:
        query = f'DELETE FROM {self.mapper.table} WHERE code = %s'

        query_data = (code,)

        with self.connection as connection:
            with connection.cursor() as cursor:
                result = cursor.execute(query, query_data) > 0

            connection.commit()

        return result