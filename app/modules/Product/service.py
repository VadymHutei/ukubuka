from modules.Product.entity import ProductEntity


class ProductService:

    def getProduct(self):
        product = {
            'id': '1',
            'name': 'Product 1',
            'description': 'Description of Product 1',
        }
        return ProductEntity(product)