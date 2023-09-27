from entities.Catalog.CatalogEntity import CatalogEntity
from entity_mappers.SQL.MySQL.Catalog.CatalogMapper import CatalogMapper
from entity_mappers.SQL.MySQL.Catalog.CatalogTextMapper import CatalogTextMapper
from repositories.SQL.MySQL.MySQLRepository import MySQLRepository
from services.Catalog.ICatalogRepository import ICatalogRepository


class CatalogRepository(MySQLRepository, ICatalogRepository):

    def get_all(self) -> list[CatalogEntity]:
        query = f'''
            SELECT
                {CatalogMapper.fields},
                {CatalogTextMapper.fields}
            FROM {CatalogMapper.table}
            JOIN {CatalogTextMapper.table}
                ON {CatalogTextMapper.field('catalog_id')} = {CatalogMapper.field('id')}
                AND {CatalogTextMapper.field('language_id')} = %s
        '''

        query_data = (
            1,
        )

        with self.connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(query, query_data)
                data = cursor.fetchall()

        return CatalogMapper.create_entities(data) if data else None # type: ignore

    def find_by_code(self, code: str) -> CatalogEntity|None:
        query = f'''
            SELECT
                {CatalogMapper.fields},
                {CatalogTextMapper.fields}
            FROM {CatalogMapper.table}
            JOIN {CatalogTextMapper.table}
                ON {CatalogTextMapper.field('catalog_id')} = {CatalogMapper.field('id')}
                AND {CatalogTextMapper.field('language_id')} = %s
            WHERE
                code = %s
            LIMIT 1
        '''

        query_data = (
            1,
            code,
        )

        with self.connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(query, query_data)
                data = cursor.fetchone()

        return CatalogMapper.create_entity(data) if data else None # type: ignore