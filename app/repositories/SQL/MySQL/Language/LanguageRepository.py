from entities.Language.LanguageEntity import LanguageEntity
from entity_mappers.SQL.MySQL.Language.LanguageMapper import LanguageMapper
from repositories.SQL.MySQL.MySQLRepository import MySQLRepository
from repositories.SQL.MySQL.PyMySQLRepository import PyMySQLRepository
from services.Language.ILanguageRepository import ILanguageRepository
from transformers.entity_transformers.SQL.MySQL.Language.LanguageEntityTransformer import LanguageEntityTransformer


class LanguageRepository(PyMySQLRepository, MySQLRepository, ILanguageRepository):

    def __init__(
        self,
        mapper: LanguageMapper,
        transformer: LanguageEntityTransformer,
    ):
        self._mapper = mapper
        self._transformer = transformer

    def find(self, language_id: int) -> LanguageEntity | None:
        query = f'''
            SELECT
                {self._mapper.fields}
            FROM
                {self._mapper.table_as_prefix}
            WHERE
                {self._mapper.pr_field('id')} = {PyMySQLRepository.PLCHLD}
        '''

        query_data = (language_id,)

        with self.connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(query, query_data)
                data = cursor.fetchone()

        return self._transformer.transform(data) if data else None
    def find_by_code(self, code: str) -> LanguageEntity | None:
        query = f'''
            SELECT
                {self._mapper.fields}
            FROM
                {self._mapper.table_as_prefix}
            WHERE
                {self._mapper.pr_field('code')} = {PyMySQLRepository.PLCHLD}
        '''

        query_data = (code,)

        with self.connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(query, query_data)
                data = cursor.fetchone()

        return self._transformer.transform(data) if data else None

    def find_all(self) -> list[LanguageEntity]:
        query = f'SELECT {self._mapper.fields} FROM {self._mapper.table_as_prefix}'

        with self.connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(query)
                data = cursor.fetchall()

        return self._transformer.transform_collection(data) if data else []

    def find_active(self) -> list[LanguageEntity]:
        query = f'''
            SELECT
                {self._mapper.fields}
            FROM
                {self._mapper.table_as_prefix}
            WHERE
                {self._mapper.pr_field('is_active')} = {PyMySQLRepository.PLCHLD}
        '''

        query_data = (1,)

        with self.connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(query, query_data)
                data = cursor.fetchall()

        return self._transformer.transform_collection(data) if data else []

    def add(self, page: LanguageEntity) -> int | None:
        query = f'INSERT INTO {self._mapper.into} VALUES ({self._mapper.fillable_placeholders})'

        query_data = self._mapper.fillable_data(page)

        with self.connection as connection:
            with connection.cursor() as cursor:
                if cursor.execute(query, query_data) == 0:
                    return None

                connection.commit()

                return cursor.lastrowid

    def update(self, page: LanguageEntity) -> bool:
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

    def delete(self, language_id: int) -> bool:
        query = f'DELETE FROM {self._mapper.table} WHERE id = {PyMySQLRepository.PLCHLD}'

        query_data = (language_id,)

        with self.connection as connection:
            with connection.cursor() as cursor:
                if cursor.execute(query, query_data) == 0:
                    return False

                connection.commit()

                return True
