class ProductRepository:

    def getProductByID(self, productID):
        query = '''
            SELECT
                `id`,
                `name`,
                `description`
            FROM
                `products`
            WHERE
                `id` = {productID}
        '''.format(productID = productID)
        result = {
            'id': '1',
            'name': 'Product 1',
            'description': 'Description of Product 1',
        }
        return result