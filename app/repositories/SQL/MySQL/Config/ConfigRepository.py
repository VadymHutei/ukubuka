from flask import g

from entities.Config.ConfigEntity import ConfigEntity
from entity_mappers.SQL.MySQL.Config.ConfigMapper import ConfigMapper
from repositories.SQL.MySQL.MySQLRepository import MySQLRepository
from repositories.SQL.MySQL.PyMySQLRepository import PyMySQLRepository
from services.Config.IConfigRepository import IConfigRepository
from transformers.entity_transformers.SQL.MySQL.Config.ConfigEntityTransformer import ConfigEntityTransformer


class ConfigRepository(PyMySQLRepository, MySQLRepository, IConfigRepository):

    def __init__(
        self,
        mapper: ConfigMapper,
        transformer: ConfigEntityTransformer,
    ):
        self._mapper = mapper
        self._transformer = transformer

    def find(self, config_id: int) -> ConfigEntity | None:
        query = f'''
            SELECT
                {self._mapper.fields}
            FROM
                {self._mapper.table_as_prefix}
            WHERE
                {self._mapper.pr_field('id')} = {PyMySQLRepository.PLCHLD}
        '''

        query_data = (g.current_language.id, config_id)

        with self.connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(query, query_data)
                data = cursor.fetchone()

        return self._transformer.transform(data) if data else None

    def find_all(self) -> list[ConfigEntity]:
        query = f'SELECT {self._mapper.fields} FROM {self._mapper.table_as_prefix}'

        query_data = (g.current_language.id,)

        with self.connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(query, query_data)
                data = cursor.fetchall()

        return self._transformer.transform_collection(data) if data else []

    def add(self, page: ConfigEntity) -> int | None:
        query = f'INSERT INTO {self._mapper.into} VALUES ({self._mapper.fillable_placeholders})'

        query_data = self._mapper.fillable_data(page)

        with self.connection as connection:
            with connection.cursor() as cursor:
                if cursor.execute(query, query_data) == 0:
                    return None

                connection.commit()

                return cursor.lastrowid

    def update(self, page: ConfigEntity) -> bool:
        set_fields_statement, set_field_values = self._mapper.get_set_data(page)

        query = f'''
            UPDATE
                {self._mapper.table}
            SET
                {set_fields_statement}
            WHERE
                {self._mapper.pr_field('id')} = {PyMySQLRepository.PLCHLD}
        '''

        query_data = (*set_field_values, page.id)

        with self.connection as connection:
            with connection.cursor() as cursor:
                if cursor.execute(query, query_data) == 0:
                    return False

                connection.commit()

                return True

    def delete(self, config_id: int) -> bool:
        query = f'DELETE FROM {self._mapper.table} WHERE id = {PyMySQLRepository.PLCHLD}'

        query_data = (config_id,)

        with self.connection as connection:
            with connection.cursor() as cursor:
                if cursor.execute(query, query_data) == 0:
                    return False

                connection.commit()

                return True
