from typing import Type

from flask import current_app as app
from pymysql import connect
from pymysql.cursors import DictCursor

from entities.Entity import Entity
from entity_mappers.SQL.SQLEntityMapper import SQLEntityMapper
from repositories.SQL.SQLRepository import SQLRepository
from transformers.entity_transformers.EntityTransformer import EntityTransformer


def _get_connection():
    credentials = {'cursorclass': DictCursor}

    credentials.update(app.config['MYSQL_DB_CREDENTIALS'])

    return connect(**credentials)


class MySQLRepository(SQLRepository):

    transformer: Type[EntityTransformer]

    @property
    def connection(self):
        return _get_connection()

    def find(self, entity_id: int) -> Entity | None:
        query = f'''
            SELECT
                {self.mapper.fields}
            FROM {self.mapper.table_as_prefix}
            WHERE
                {self.mapper.table_prefix}.id = {SQLEntityMapper.QUERY_PLACEHOLDER}
        '''

        query_data = entity_id

        with self.connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(query, query_data)
                data = cursor.fetchone()

        return self.transformer.transform(data) if data else None

    def find_all(self) -> list[Entity]:
        query = f'''
            SELECT
                {self.mapper.fields}
            FROM {self.mapper.table_as_prefix}
        '''

        with self.connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(query)
                data = cursor.fetchall()

        return self.transformer.transform_collection(data) if data else []

    def add(self, entity: Entity) -> bool:
        query = f'''
            INSERT INTO {self.mapper.table} ({self.mapper.fillable_fields})
            VALUES ({self.mapper.fillable_placeholders()})
        '''

        query_data = self.mapper.fillable_data(entity)

        with self.connection as connection:
            with connection.cursor() as cursor:
                result = cursor.execute(query, query_data) > 0

            connection.commit()

        return result

    def update(self, entity: Entity) -> bool:
        set_fields_statement, set_field_values = self.mapper.get_set_data(entity)

        query = f'''
            UPDATE {self.mapper.table}
            SET {set_fields_statement}
            WHERE id = {SQLEntityMapper.QUERY_PLACEHOLDER}
        '''

        query_data = (*set_field_values, entity.id)

        with self.connection as connection:
            with connection.cursor() as cursor:
                result = cursor.execute(query, query_data) > 0

            connection.commit()

        return result

    def delete(self, entity_id: int) -> bool:
        query = f'DELETE FROM {self.mapper.table} WHERE id = {SQLEntityMapper.QUERY_PLACEHOLDER}'

        query_data = (entity_id,)

        with self.connection as connection:
            with connection.cursor() as cursor:
                result = cursor.execute(query, query_data) > 0

            connection.commit()

        return result