from entities.Entity import Entity
from entities.TextEntity import TextEntity
from entity_mappers.SQL.SQLEntityMapper import SQLEntityMapper
from repositories.SQL.MySQL.CodeRepository import CodeRepository
from repositories.SQL.MySQL.TextRepository import TextRepository


class CodeTextRepository(CodeRepository, TextRepository):

    def find_by_code(self, code: str) -> Entity | None:
        query = f'''
            SELECT
                {self.mapper.fields},
                {self.text_mapper.fields}
            FROM {self.mapper.table_as_prefix}
            LEFT JOIN {self.text_mapper.table_as_prefix}
                ON {self.text_mapper.entity_foreign_key_field_with_prefix} = {self.mapper.pr_id_field}
            WHERE
                {self.mapper.pr_field('code')} = {SQLEntityMapper.QUERY_PLACEHOLDER}
        '''

        query_data = (code,)

        with self.connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(query, query_data)
                data = cursor.fetchone()

        return self.transformer.transform(data) if data else None

    def find_translations_by_entity_code(self, entity_code: str) -> list[TextEntity]:
        query = f'''
            SELECT
                {self.text_mapper.fields}
            FROM {self.text_mapper.table_as_prefix}
            JOIN {self.mapper.table_as_prefix}
                ON {self.mapper.pr_id_field} = {self.text_mapper.entity_foreign_key_field_with_prefix}
            WHERE
                {self.mapper.pr_field('code')} = {SQLEntityMapper.QUERY_PLACEHOLDER}
        '''

        query_data = (entity_code,)

        with self.connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(query, query_data)
                data = cursor.fetchall()

        return self.translation_transformer.transform_collection(data) if data else []