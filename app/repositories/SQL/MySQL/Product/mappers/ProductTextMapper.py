from entities.Product.ProductTextEntity import ProductTextEntity


class ProductTextMapper:

    FIELDS = [
        'id',
        'product_id',
        'language_id',
        'name',
        'description',
        'created_at',
        'updated_at',
    ]

    def from_row(self, row: dict) -> dict:
        return ProductTextEntity(
            id=int(row['id']),
            product_id=int(row['product_id']),
            language_id=int(row['language_id']),
            name=row['name'],
            description=row['description'],
            created_at=row['created_at'],
            updated_at=row['updated_at'],
        )