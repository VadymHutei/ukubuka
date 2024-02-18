from flask import g

from entities.Entity import Entity
from entities.TextEntity import TextEntity
from entity_mappers.SQL.MySQL.Page.PageMapper import PageMapper
from entity_mappers.SQL.MySQL.Page.PageTextMapper import PageTextMapper
from entity_mappers.SQL.SQLEntityMapper import SQLEntityMapper
from repositories.SQL.MySQL.MySQLRepository import MySQLRepository
from services.Page.IPageRepository import IPageRepository
from transformers.entity_transformers.SQL.MySQL.Page.PageEntityTransformer import PageEntityTransformer
from transformers.entity_transformers.SQL.MySQL.Page.PageTextEntityTransformer import PageTextEntityTransformer


class PageRepository(IPageRepository, MySQLRepository):

    mapper = PageMapper
    text_mapper = PageTextMapper
    transformer = PageEntityTransformer
    translation_transformer = PageTextEntityTransformer

    def find(self, entity_id: int) -> Entity | None:
        query = f'''
            SELECT
                {self.mapper.fields}
            FROM {self.mapper.table_as_prefix}
            WHERE
                {self.mapper.pr_id_field} = {self.mapper.QUERY_PLACEHOLDER}
        '''

        query_data = (entity_id,)

        with self.connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(query, query_data)
                data = cursor.fetchone()

        return self.transformer.transform(data) if data else None

    def find_all(self) -> list[Entity]:
        query = f'''
            SELECT
                {self.mapper.fields},
                {self.text_mapper.fields}
            FROM {self.mapper.table_as_prefix}
            LEFT JOIN {self.text_mapper.table_as_prefix}
                ON {self.text_mapper.entity_foreign_key_field_with_prefix} = {self.mapper.pr_field('id')}
                AND {self.text_mapper.language_foreign_key_field_with_prefix} = {SQLEntityMapper.QUERY_PLACEHOLDER}
        '''

        query_data = (g.current_language.id,)

        with self.connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(query, query_data)
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

    def find_translation(self, entity_text_id: int) -> TextEntity | None:
        query = f'''
            SELECT
                {self.text_mapper.fields}
            FROM {self.text_mapper.table_as_prefix}
            WHERE
                {self.text_mapper.table_prefix}.id = {SQLEntityMapper.QUERY_PLACEHOLDER}
        '''

        query_data = (entity_text_id,)

        with self.connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(query, query_data)
                data = cursor.fetchone()

        return self.translation_transformer.transform(data) if data else None

    def find_translations_by_entity_id(self, entity_id: int) -> list[TextEntity]:
        query = f'''
            SELECT
                {self.text_mapper.fields}
            FROM {self.text_mapper.table_as_prefix}
            JOIN {self.mapper.table_as_prefix}
                ON {self.mapper.pr_id_field} = {self.text_mapper.entity_foreign_key_field_with_prefix}
            WHERE
                {self.mapper.pr_field('id')} = {SQLEntityMapper.QUERY_PLACEHOLDER}
        '''

        query_data = (entity_id,)

        with self.connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(query, query_data)
                data = cursor.fetchall()

        return self.translation_transformer.transform_collection(data) if data else []

    def add_translation(self, text: TextEntity) -> bool:
        query = f'''
            INSERT INTO {self.text_mapper.table} ({self.text_mapper.fillable_fields})
            VALUES ({self.text_mapper.fillable_placeholders()})
        '''

        query_data = self.text_mapper.fillable_data(text)

        with self.connection as connection:
            with connection.cursor() as cursor:
                result = cursor.execute(query, query_data) > 0

            connection.commit()

        return result

    def update_translation(self, text: TextEntity) -> bool:
        set_fields_statement, set_field_values = self.text_mapper.get_set_data(text)

        query = f'''
            UPDATE {self.text_mapper.table}
            SET {set_fields_statement}
            WHERE id = {SQLEntityMapper.QUERY_PLACEHOLDER}
        '''

        query_data = (*set_field_values, text.id,)

        with self.connection as connection:
            with connection.cursor() as cursor:
                result = cursor.execute(query, query_data) > 0

            connection.commit()

        return result

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

    def delete_by_code(self, code: str) -> bool:
        query = f'DELETE FROM {self.mapper.table} WHERE code = {SQLEntityMapper.QUERY_PLACEHOLDER}'

        query_data = (code,)

        with self.connection as connection:
            with connection.cursor() as cursor:
                result = cursor.execute(query, query_data) > 0

            connection.commit()

        return result

    def find_active(self) -> list[Entity]:
        query = f'''
            SELECT
                {self.mapper.fields}
            FROM {self.mapper.table_as_prefix}
            WHERE {self.mapper.pr_field('is_active')} = 1
        '''

        with self.connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(query)
                data = cursor.fetchall()

        return self.transformer.transform_collection(data) if data else []