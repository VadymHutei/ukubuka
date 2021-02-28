from entities.RequestedResource import RequestedResource


class ShopPathResolver:

    CATALOG_ID_TYPE = 'catalogID'
    CATALOG_ALIAS_TYPE = 'catalogAlias'
    CATEGORY_ID_TYPE = 'categoryID'
    CATEGORY_ALIAS_TYPE = 'categoryAlias'
    PRODUCT_ID_TYPE = 'productID'
    PRODUCT_ALIAS_TYPE = 'productAlias'
    SKU_ID_TYPE = 'SKUID'
    SKU_ALIAS_TYPE = 'SKUAlias'

    def __init__(self, validator):
        self.validator = validator
        self.requestedResource = RequestedResource()

    def resolve(self, path):
        path = path.split('/')
        lastSegment = path[-1]
        if self.validator.catalogAlias(lastSegment)
            catalog = self.repository.getCatalogByAlias(lastSegment)
            if catalog:
                self.requestedResource.isValidPath = True
                self.requestedResource.resourceType = self.CATEGORY_ALIAS_TYPE
                self.requestedResource.isCatalog = True

        return self.requestedResource

    def _getTypeValidators(self):
        return {
            CATEGORY_ID_TYPE: validator.categoryID,
            CATEGORY_ALIAS_TYPE: validator.categoryAlias,
            PRODUCT_ID_TYPE: validator.productID,
            PRODUCT_ALIAS_TYPE: validator.productAlias,
            SKU_ID_TYPE: validator.SKUID,
            SKU_ALIAS_TYPE: validator.SKUAlias
        }