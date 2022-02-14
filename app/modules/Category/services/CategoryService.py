from modules.Category.entities.CategoryEntity import CategoryEntity
from modules.Category.repositories.CategoryRepository import CategoryRepository


class CategoryService:

    def __init__(self):
        self._categoryRepository = CategoryRepository()

    def getCategories(self):
        categoriesData = self._categoryRepository.getCategories()
        return [CategoryEntity(row) for row in categoriesData]

    def getSubcategoryIDs(self, categoryIDs):
        if isinstance(categoryIDs, int):
            categoryIDs = [categoryIDs]

        result = categoryIDs
        
        if not categoryIDs:
            return result

        categories = self._categoryRepository.getAllSubcategories(categoryIDs)
        count = 1
        while count > 0:
            count = 0
            for category in categories:
                if category['parent_id'] in result and category['id'] not in result:
                    result.append(category['id'])
                    count += 1
        return result

    def getProductsByCategoryIDs(self, categoryIDs):
        products = self._categoryRepository.getProductsByCategoryIDs(categoryIDs)
        productIDs = [product['id'] for product in products]
        productNumericCharacteristics = self._categoryRepository.getNumericCharacteristicsByProductIDs(productIDs)
        productTextCharacteristics = self._categoryRepository.getTextCharacteristicsByProductIDs(productIDs)
        for product in products:
            product['characteristics'] = {}
            for productNumericCharacteristic in productNumericCharacteristics:
                if product['id'] == productNumericCharacteristic['product_id']:
                    product['characteristics'][productNumericCharacteristic['characteristic_id']] = productNumericCharacteristic['value']
            for productTextCharacteristic in productTextCharacteristics:
                if product['id'] == productTextCharacteristic['product_id']:
                    product['characteristics'][productTextCharacteristic['characteristic_id']] = productTextCharacteristic['value']
        return products