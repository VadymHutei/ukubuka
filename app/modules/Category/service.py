from modules.Category.repository import CategoryRepository


class CategoryService:

    def __init__(self):
        self.repository = CategoryRepository()

    def getSubcategoryIDs(self, categoryIDs):
        if isinstance(categoryIDs, int):
            categoryIDs = [categoryIDs]

        result = categoryIDs
        
        if not categoryIDs:
            return result

        categories = self.repository.getAllSubcategories(categoryIDs)
        count = 1
        while count > 0:
            count = 0
            for category in categories:
                if category['parent_id'] in result and category['id'] not in result:
                    result.append(category['id'])
                    count += 1
        return result

    def getProductsByCategoryIDs(self, categoryIDs):
        products = self.repository.getProductsByCategoryIDs(categoryIDs)
        productIDs = [product['id'] for product in products]
        productNumericCharacteristics = self.repository.getNumericCharacteristicsByProductIDs(productIDs)
        productTextCharacteristics = self.repository.getTextCharacteristicsByProductIDs(productIDs)
        for product in products:
            product['characteristics'] = {}
            for productNumericCharacteristic in productNumericCharacteristics:
                if product['id'] == productNumericCharacteristic['product_id']:
                    product['characteristics'][productNumericCharacteristic['characteristic_id']] = productNumericCharacteristic['value']
            for productTextCharacteristic in productTextCharacteristics:
                if product['id'] == productTextCharacteristic['product_id']:
                    product['characteristics'][productTextCharacteristic['characteristic_id']] = productTextCharacteristic['value']
        print(productNumericCharacteristics)
        print(productTextCharacteristics)
        print(products)
        return products