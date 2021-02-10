from modules.Catalog.entity import CatalogEntity


class CatalogService:

    def getProducts(self):
        products = [
            {
                'id': '1',
                'name': 'Product 1'
            },
            {
                'id': '2',
                'name': 'Product 2'
            }
        ]
        return CatalogEntity(products)