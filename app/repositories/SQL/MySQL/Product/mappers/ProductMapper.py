from entities.Product.ProductEntity import ProductEntity
from repositories.SQL.SQLMapper import SQLMapper


class ProductMapper(SQLMapper):

    _ENTITY_CLASS = ProductEntity

    _TABLE_PREFIX = 'p'

    _FIELDS = [
        'id',
        'code',
        'is_active',
        'created_at',
        'updated_at',
        'deleted_at',
    ]

    _CAST = {
        'id': int,
        'is_active': bool,
    }

    def from_row(self, row: dict) -> dict:
        return ProductEntity(
            id=int(row['id']),
            code=row['code'],
            is_active=bool(row['is_active']),
            created_at=row['created_at'],
            updated_at=row['updated_at'],
            deleted_at=row['deleted_at'],
        )

    def from_rows(self, rows: list|tuple) -> dict[str, ProductEntity]:
        products = {}

        for row in rows:
            product = self.from_row(row)
            products[product.code] = product

        return products