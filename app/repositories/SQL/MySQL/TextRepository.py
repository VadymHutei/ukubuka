from typing import Type

from flask import g

from entities.Entity import Entity
from entities.TextEntity import TextEntity
from entity_mappers.SQL.SQLEntityMapper import SQLEntityMapper
from repositories.SQL.MySQL.MySQLRepository import MySQLRepository
from transformers.entity_transformers.EntityTransformer import EntityTransformer


class TextRepository(MySQLRepository):

    translation_transformer: Type[EntityTransformer]

    def find(self, id: int) -> Entity | None:
        query = f'''
            SELECT
                {self.mapper.fields},
                {self.text_mapper.fields}
            FROM {self.mapper.table_as_prefix}
            LEFT JOIN {self.text_mapper.table_as_prefix}
                ON {self.text_mapper.pr_entity_foreign_key_field} = {self.mapper.pr_field('id')}
                AND {self.text_mapper.pr_language_foreign_key_field} = {SQLEntityMapper.PLCHLD}
            WHERE
                {self.mapper.table_prefix}.id = {SQLEntityMapper.PLCHLD}
        '''

        query_data = (g.current_language.id, id)

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
                ON {self.text_mapper.pr_entity_foreign_key_field} = {self.mapper.pr_field('id')}
                AND {self.text_mapper.pr_language_foreign_key_field} = {SQLEntityMapper.PLCHLD}
        '''

        query_data = (g.current_language.id,)

        with self.connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(query, query_data)
                data = cursor.fetchall()

        return self.transformer.transform_collection(data) if data else []

    def add_translation(self, text: TextEntity) -> bool:
        query = f'''
            INSERT INTO {self.text_mapper.table} ({self.text_mapper.fillable_fields})
            VALUES ({self.text_mapper.fillable_placeholders})
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
            WHERE id = {SQLEntityMapper.PLCHLD}
        '''

        query_data = (*set_field_values, text.id,)

        with self.connection as connection:
            with connection.cursor() as cursor:
                result = cursor.execute(query, query_data) > 0

            connection.commit()

        return result

    def find_translation(self, id: int) -> TextEntity | None:
        query = f'''
            SELECT
                {self.text_mapper.fields}
            FROM {self.text_mapper.table_as_prefix}
            WHERE
                {self.text_mapper.table_prefix}.id = {SQLEntityMapper.PLCHLD}
        '''

        query_data = (id,)

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
                ON {self.mapper.pr_id_field} = {self.text_mapper.pr_entity_foreign_key_field}
            WHERE
                {self.mapper.pr_field('id')} = {SQLEntityMapper.PLCHLD}
        '''

        query_data = (entity_id,)

        with self.connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(query, query_data)
                data = cursor.fetchall()

        return self.translation_transformer.transform_collection(data) if data else []