from ukubuka.AbstractService import AbstractService


class ShopService(AbstractService):

    def __init__(self, repository):
        self._repository = repository

    def getCatalogByAlias(self, catalogAlias):
        return self._repository.getCatalogByAlias(catalogAlias)

    def getCatalogById(self, catalogID):
        return self._repository.getCatalogById(catalogID)

    def getCategoryByAlias(self, categoryAlias):
        return self._repository.getCategoryByAlias(categoryAlias)

    def getCategoryByID(self, categoryID):
        return self._repository.getCategoryByID(categoryID)

    def getProductByAlias(self, productAlias):
        return self._repository.getProductByAlias(productAlias)

    def getProductByID(self, productID):
        return self._repository.getProductByID(productID)

    def getSKUByAlias(self, SKUAlias):
        return self._repository.getSKUByAlias(SKUAlias)

    def getSKUByID(self, SKUID):
        return self._repository.getSKUByID(SKUID)