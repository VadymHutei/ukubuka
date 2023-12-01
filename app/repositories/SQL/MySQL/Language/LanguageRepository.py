from entities.Language.LanguageEntity import LanguageEntity
from entity_mappers.SQL.MySQL.Language.LanguageMapper import LanguageMapper
from repositories.SQL.MySQL.MySQLRepository import MySQLRepository
from services.Language.ILanguageRepository import ILanguageRepository
from value_objects.Language.LanguageVO import LanguageVO


class LanguageRepository(MySQLRepository, ILanguageRepository):

    def add(self, vo: LanguageVO) -> bool:
        placeholders = ', '.join(['%s'] * LanguageMapper.fillable_length)

        query = f'INSERT INTO {LanguageMapper.table} ({LanguageMapper.fillable}) VALUES ({placeholders})'

        query_data = LanguageMapper.fillable_data(vo)

        with self.connection as connection:
            with connection.cursor() as cursor:
                result = cursor.execute(query, query_data) > 0

            connection.commit()

        return result

    def get_by_id(self, id: int) -> LanguageEntity:
        query = f'''
            SELECT
                {LanguageMapper.fields}
            FROM {LanguageMapper.table_as_prefix}
            WHERE {LanguageMapper.field('id')} = %s
        '''

        query_data = (id,)

        with self.connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(query, query_data)
                data = cursor.fetchone()

        return LanguageMapper.create_entity(data)

    def get_by_code(self, code: str) -> LanguageEntity:
        query = f'''
            SELECT
                {LanguageMapper.fields}
            FROM {LanguageMapper.table_as_prefix}
            WHERE {LanguageMapper.field('code')} = %s
        '''

        query_data = (code,)

        with self.connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(query, query_data)
                data = cursor.fetchone()

        return LanguageMapper.create_entity(data)

    def find_all(self) -> list[LanguageEntity] | None:
        query = f'''
            SELECT
                {LanguageMapper.fields}
            FROM {LanguageMapper.table_as_prefix}
        '''

        with self.connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(query)
                data = cursor.fetchall()

        return LanguageMapper.create_entities(data) if data else None

    def find_by_id(self, id: int) -> LanguageEntity | None:
        query = f'''
            SELECT
                {LanguageMapper.fields}
            FROM {LanguageMapper.table_as_prefix}
            WHERE {LanguageMapper.field('id')} = %s
        '''

        query_data = (id,)

        with self.connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(query, query_data)
                data = cursor.fetchone()

        return LanguageMapper.create_entity(data) if data else None

    def find_by_code(self, code: str) -> LanguageEntity | None:
        query = f'''
            SELECT
                {LanguageMapper.fields}
            FROM {LanguageMapper.table_as_prefix}
            WHERE {LanguageMapper.field('code')} = %s
        '''

        query_data = (code,)

        with self.connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(query, query_data)
                data = cursor.fetchone()

        return LanguageMapper.create_entity(data) if data else None

    def update(self, entity: LanguageEntity) -> bool:
        set_fields_statement, set_field_values = LanguageMapper.get_set_data(entity)

        query = f'UPDATE {LanguageMapper.table} SET {set_fields_statement} WHERE id = %s'

        query_data = (*set_field_values, entity.id,)

        with self.connection as connection:
            with connection.cursor() as cursor:
                result = cursor.execute(query, query_data) > 0

            connection.commit()

        return result

    def delete_by_code(self, code: str) -> bool:
        query = f'DELETE FROM {LanguageMapper.table} WHERE code = %s'

        query_data = (code,)

        with self.connection as connection:
            with connection.cursor() as cursor:
                result = cursor.execute(query, query_data) > 0

            connection.commit()

        return result

    def get_only_active(self) -> list[LanguageEntity]:
        query = f'''
            SELECT
                {LanguageMapper.fields}
            FROM {LanguageMapper.table_as_prefix}
            WHERE {LanguageMapper.field('is_active')} = 1
        '''

        with self.connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(query)
                data = cursor.fetchall()

        return LanguageMapper.create_entities(data)