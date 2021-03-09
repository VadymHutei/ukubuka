from entities.RequestedResource import RequestedResource
from modules.Shop.validator import ShopValidator


class ShopPathResolver:

    CATALOG_ID_TYPE = 'catalogID'
    CATALOG_ALIAS_TYPE = 'catalogAlias'
    CATEGORY_ID_TYPE = 'categoryID'
    CATEGORY_ALIAS_TYPE = 'categoryAlias'
    PRODUCT_ID_TYPE = 'productID'
    PRODUCT_ALIAS_TYPE = 'productAlias'
    SKU_ID_TYPE = 'SKUID'
    SKU_ALIAS_TYPE = 'SKUAlias'

    def __init__(self, service):
        self.service = service
        self.requestedResource = RequestedResource()

    def resolve(self, path):
        path = path.split('/')
        lastSegment = path[-1]
        for resource in self._getTypeValidators():
            if resource['validationFunction'](lastSegment):
                data = resource['serviceFunction'](lastSegment)
                if data:
                    self.requestedResource.isValidPath = True
                    self.requestedResource.resourceType = resource['type']
                    if resource['pageType'] == 'isCatalog':
                        self.requestedResource.isCatalog = True
                    elif resource['pageType'] == 'isProduct':
                        self.requestedResource.isProduct = True
                    break

        return self.requestedResource

    def _getTypeValidators(self):
        return [
            {
                'type': self.CATALOG_ID_TYPE,
                'validationFunction': ShopValidator.catalogID,
                'serviceFunction': self.service.getCatalogByAlias
            },
            {
                'type': self.CATALOG_ALIAS_TYPE,
                'validationFunction': ShopValidator.catalogAlias,
                'serviceFunction': self.service.getCatalogById
            },
            {
                'type': self.CATEGORY_ID_TYPE,
                'validationFunction': ShopValidator.categoryID,
                'serviceFunction': self.service.getCategoryByAlias
            },
            {
                'type': self.CATEGORY_ALIAS_TYPE,
                'validationFunction': ShopValidator.categoryAlias,
                'serviceFunction': self.service.getCategoryByAlias
            },
            {
                'type': self.PRODUCT_ID_TYPE,
                'validationFunction': ShopValidator.productID,
                'serviceFunction': self.service.getProductByAlias
            },
            {
                'type': self.PRODUCT_ALIAS_TYPE,
                'validationFunction': ShopValidator.productAlias,
                'serviceFunction': self.service.getProductByAlias
            },
            {
                'type': self.SKU_ID_TYPE,
                'validationFunction': ShopValidator.SKUID,
                'serviceFunction': self.service.getSKUByAlias
            },
            {
                'type': self.SKU_ALIAS_TYPE,
                'validationFunction': ShopValidator.SKUAlias,
                'serviceFunction': self.service.getSKUByAlias
            }
        ]