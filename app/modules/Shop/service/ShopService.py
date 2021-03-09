from ukubuka.AbstractService import AbstractService


class ShopService(AbstractService):
    
    def __init__(self, repository):
        self.repository = repository

    def getCatalogByAlias(self, alias):
        return self.repository.getCatalogByAlias(alias)

    def getCatalogById(self, segment):
        return []

    def getCategoryByAlias(self, segment):
        return []

    def getCategoryByAlias(self, segment):
        return []

    def getProductByAlias(self, segment):
        return []

    def getProductByAlias(self, segment):
        return []

    def getSKUByAlias(self, segment):
        return []

    def getSKUByAlias(self, segment):
        return []