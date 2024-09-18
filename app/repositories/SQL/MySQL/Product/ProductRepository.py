from flask import g

from entities.Product.ProductEntity import ProductEntity
from repositories.SQL.MySQL.MySQLRepository import MySQLRepository
from repositories.SQL.MySQL.Product.mappers.ProductMapper import ProductMapper
from repositories.SQL.MySQL.Product.mappers.ProductTextMapper import ProductTextMapper
from repositories.SQL.MySQL.Product.transformers.ProductEntityTransformer import ProductEntityTransformer
from repositories.SQL.MySQL.PyMySQLRepository import PyMySQLRepository
from services.Product.IProductRepository import IProductRepository


class ProductRepository(PyMySQLRepository, MySQLRepository, IProductRepository):

    def __init__(
        self,
        mapper: ProductMapper,
        text_mapper: ProductTextMapper,
        transformer: ProductEntityTransformer,
    ):
        self._mapper = mapper
        self._text_mapper = text_mapper
        self._transformer = transformer

    def find_by_slug(self, slug: str, only_active: bool = False) -> ProductEntity | None:
        only_active_condition = f'AND {self._mapper.pr_field('is_active')} = 1' if only_active else ''

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
                {self._mapper.pr_field('slug')} = {PyMySQLRepository.PLCHLD}
                {only_active_condition}
        '''

        query_data = (g.current_language.id, slug)

        with self.connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(query, query_data)
                data = cursor.fetchone()

        return self._transformer.transform(data) if data else None
