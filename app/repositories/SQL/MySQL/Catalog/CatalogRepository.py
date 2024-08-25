from flask import g

from entities.Catalog.CatalogEntity import CatalogEntity
from repositories.SQL.MySQL.Catalog.mappers.CatalogMapper import CatalogMapper
from repositories.SQL.MySQL.Catalog.mappers.CatalogTextMapper import CatalogTextMapper
from repositories.SQL.MySQL.Catalog.transformers.CatalogEntityTransformer import CatalogEntityTransformer
from repositories.SQL.MySQL.MySQLRepository import MySQLRepository
from repositories.SQL.MySQL.PyMySQLRepository import PyMySQLRepository
from services.Catalog.ICatalogRepository import ICatalogRepository


class CatalogRepository(PyMySQLRepository, MySQLRepository, ICatalogRepository):

    def __init__(
        self,
        mapper: CatalogMapper,
        text_mapper: CatalogTextMapper,
        transformer: CatalogEntityTransformer,
    ):
        self._mapper = mapper
        self._transformer = transformer
        self._text_mapper = text_mapper

    def find(self, page_id: int) -> CatalogEntity | None:
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
    def find_all(self) -> list[CatalogEntity]:
        pass
    def add(self, catalog: CatalogEntity) -> int | None:
        pass
    def update(self, catalog: CatalogEntity) -> bool:
        pass
    def delete(self, catalog_id: int) -> bool:
        pass