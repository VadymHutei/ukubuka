from flask import g

from entities.Page.PageEntity import PageEntity
from entity_mappers.SQL.MySQL.Page.PageMapper import PageMapper
from entity_mappers.SQL.MySQL.Page.PageTextMapper import PageTextMapper
from repositories.SQL.MySQL.MySQLRepository import MySQLRepository
from repositories.SQL.MySQL.PyMySQLRepository import PyMySQLRepository
from services.Page.IPageRepository import IPageRepository
from transformers.entity_transformers.SQL.MySQL.Page.PageEntityTransformer import PageEntityTransformer


class PageRepository(PyMySQLRepository, MySQLRepository, IPageRepository):

    def __init__(
        self,
        mapper: PageMapper,
        text_mapper: PageTextMapper,
        transformer: PageEntityTransformer,
    ):
        self._mapper = mapper
        self._transformer = transformer
        self._text_mapper = text_mapper

    def find(self, page_id: int) -> PageEntity | None:
        query = f'''
            SELECT
                {self._mapper.fields},
                {self._text_mapper.entity_fields}
            FROM
                {self._mapper.table_as_prefix}
                LEFT JOIN {self._text_mapper.table_as_prefix}
                    ON {self._text_mapper.pr_entity_foreign_key_field} = {self._mapper.pr_field('id')}
                    AND {self._text_mapper.pr_language_foreign_key_field} = {PyMySQLRepository.PLCHLD}
            WHERE
                {self._mapper.pr_field('id')} = {PyMySQLRepository.PLCHLD}
        '''

        query_data = (g.current_language.id, page_id)

        with self.connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(query, query_data)
                data = cursor.fetchone()

        return self._transformer.transform(data) if data else None

    def find_by_code(self, code: str) -> PageEntity | None:
        query = f'''
            SELECT
                {self._mapper.fields},
                {self._text_mapper.entity_fields}
            FROM
                {self._mapper.table_as_prefix}
                LEFT JOIN {self._text_mapper.table_as_prefix}
                    ON {self._text_mapper.pr_entity_foreign_key_field} = {self._mapper.pr_field('id')}
                    AND {self._text_mapper.pr_language_foreign_key_field} = {PyMySQLRepository.PLCHLD}
            WHERE
                {self._mapper.pr_field('code')} = {PyMySQLRepository.PLCHLD}
        '''

        query_data = (g.current_language.id, code)

        with self.connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(query, query_data)
                data = cursor.fetchone()

        return self._transformer.transform(data) if data else None

    def find_all(self) -> list[PageEntity]:
        query = f'''
            SELECT
                {self._mapper.fields},
                {self._text_mapper.fields}
            FROM
                {self._mapper.table_as_prefix}
                LEFT JOIN {self._text_mapper.table_as_prefix}
                    ON {self._text_mapper.pr_entity_foreign_key_field} = {self._mapper.pr_field('id')}
                    AND {self._text_mapper.pr_language_foreign_key_field} = {PyMySQLRepository.PLCHLD}
        '''

        query_data = (g.current_language.id,)

        with self.connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(query, query_data)
                data = cursor.fetchall()

        return self._transformer.transform_collection(data) if data else []

    def add(self, page: PageEntity) -> int | None:
        query = f'''
            INSERT
                INTO {self._mapper.into}
            VALUES
                ({self._mapper.fillable_placeholders})
        '''

        query_data = self._mapper.fillable_data(page)

        with self.connection as connection:
            with connection.cursor() as cursor:
                if cursor.execute(query, query_data) == 0:
                    return None

                connection.commit()

                return cursor.lastrowid

    def update(self, page: PageEntity) -> bool:
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

    def delete(self, page_id: int) -> bool:
        query = f'DELETE FROM {self._mapper.table} WHERE id = {PyMySQLRepository.PLCHLD}'

        query_data = (page_id,)

        with self.connection as connection:
            with connection.cursor() as cursor:
                if cursor.execute(query, query_data) == 0:
                    return False

                connection.commit()

                return True

    def delete_by_code(self, code: str) -> bool:
        query = f'DELETE FROM {self._mapper.table} WHERE code = {PyMySQLRepository.PLCHLD}'

        query_data = (code,)

        with self.connection as connection:
            with connection.cursor() as cursor:
                if cursor.execute(query, query_data) == 0:
                    return False

                connection.commit()

                return True
