from typing import Optional

from repositories.SQL.SQLRepository import SQLRepository
from services.Product.ProductRepositoryInterface import ProductRepositoryInterface
from repositories.SQL.MySQL.Product.mappers.ProductPriceMapper import ProductPriceMapper
from repositories.SQL.MySQL.Product.mappers.ProductTextMapper import ProductTextMapper
from repositories.SQL.MySQL.Product.mappers.ProductMapper import ProductMapper
from entities.Product.ProductEntity import ProductEntity


class ProductRepository(SQLRepository, ProductRepositoryInterface):

    def find_by_code(self, code: str) -> Optional[ProductEntity]:
        query = f'''
            SELECT
                {ProductMapper.fields},
                {ProductTextMapper.fields},
                {ProductPriceMapper.fields}
            FROM {ProductMapper.table}
            JOIN {ProductTextMapper.table}
                ON {ProductTextMapper.table_prefix}.product_id = {ProductMapper.table_prefix}.id
                AND {ProductTextMapper.table_prefix}.language_id = %s
            JOIN {ProductPriceMapper.table}
                ON {ProductPriceMapper.table_prefix}.product_id = {ProductMapper.table_prefix}.id
            WHERE
                {ProductMapper.table_prefix}.code = %s
        '''

        with self.connection as connection:
            with connection.cursor() as cursor:
                # cursor.execute(query, (g.current_language.id, code))
                cursor.execute(query, (1, code))
                data = cursor.fetchone()

        return ProductMapper.create_entity(data) if data else None