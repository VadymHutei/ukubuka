from typing import Optional

from flask import g

from repositories.SQL.SQLRepository import SQLRepository
from services.Product.ProductRepository import ProductRepository as ProductRepositoryInterface
from repositories.SQL.MySQL.Product.mappers.ProductPriceMapper import ProductPriceMapper
from repositories.SQL.MySQL.Product.mappers.ProductTextMapper import ProductTextMapper
from repositories.SQL.MySQL.Product.mappers.ProductMapper import ProductMapper
from entities.Product.ProductEntity import ProductEntity


class ProductRepository(SQLRepository, ProductRepositoryInterface):

    def find_by_code(self, code: str) -> Optional[ProductEntity]:
        query = f'''
            SELECT
                {ProductMapper.get_fields()},
                {ProductTextMapper.get_fields()},
                {ProductPriceMapper.get_fields()}
            FROM {ProductMapper.get_table()}
            JOIN {ProductTextMapper.get_table()}
                ON {ProductTextMapper._TABLE_PREFIX}.product_id = {ProductMapper._TABLE_PREFIX}.id
                AND {ProductTextMapper._TABLE_PREFIX}.language_id = %s
            JOIN {ProductPriceMapper.get_table()}
                ON {ProductPriceMapper._TABLE_PREFIX}.product_id = {ProductMapper._TABLE_PREFIX}.id
            WHERE
                {ProductMapper._TABLE_PREFIX}.code = %s
        '''

        with self.connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(query, (g.current_language.id, code))
                data = cursor.fetchone()

        return ProductMapper.create_entity(data) if data else None