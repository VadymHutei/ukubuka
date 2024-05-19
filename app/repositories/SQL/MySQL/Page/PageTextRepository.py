from flask import g

from entities.Page.PageTextEntity import PageTextEntity
from entity_mappers.SQL.MySQL.Page.PageTextMapper import PageTextMapper
from repositories.SQL.MySQL.MySQLRepository import MySQLRepository
from repositories.SQL.MySQL.PyMySQLRepository import PyMySQLRepository
from services.Page.IPageTextRepository import IPageTextRepository
from transformers.entity_transformers.SQL.MySQL.Page.PageTextEntityTransformer import PageTextEntityTransformer


class PageTextRepository(PyMySQLRepository, MySQLRepository, IPageTextRepository):

    def __init__(
        self,
        mapper: PageTextMapper,
        transformer: PageTextEntityTransformer,
    ):
        self._mapper = mapper
        self._transformer = transformer

    def find(self, page_text_id: int) -> PageTextEntity | None:
        query = f'''
            SELECT
                {self._mapper.fields}
            FROM
                {self._mapper.table_as_prefix}
            WHERE
                {self._mapper.pr_field('id')} = {PyMySQLRepository.PLCHLD}
        '''

        query_data = (g.current_language.id, page_text_id)

        with self.connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(query, query_data)
                data = cursor.fetchone()

        return self._transformer.transform(data) if data else None

    def find_all(self) -> list[PageTextEntity]:
        query = f'''
            SELECT
                {self._mapper.fields}
            FROM
                {self._mapper.table_as_prefix}
        '''

        query_data = (g.current_language.id,)

        with self.connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(query, query_data)
                data = cursor.fetchall()

        return self._transformer.transform_collection(data) if data else []

    def add(self, page: PageTextEntity) -> int | None:
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

    def update(self, page: PageTextEntity) -> bool:
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

    def delete(self, page_text_id: int) -> bool:
        query = f'DELETE FROM {self._mapper.table} WHERE id = {PyMySQLRepository.PLCHLD}'

        query_data = (page_text_id,)

        with self.connection as connection:
            with connection.cursor() as cursor:
                if cursor.execute(query, query_data) == 0:
                    return False

                connection.commit()

                return True
