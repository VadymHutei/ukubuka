from modules.Catalog.repository import CatalogRepository


class CatalogService:

    def __init__(self):
        self.repository = CatalogRepository()

        def getCatalogByAlias(self, catalogAlias):
            return self.repository.getCatalogByAlias(categoryAlias)

        def getProductsByCatalogID(self, catalogID):
            catalogCategoriesID = self.getCategoriesIDByCatalogID(catalogID)
            catalogProducts = self.repository.getProductsByCatalogID(catalogID) + self.repository.getProductsByCategoriesID(catalogCategoriesID)

        def getCategoriesIDByCatalogID(self, catalogID):
            categories = self.repository.getCategoriesByCatalogID(catalogID)
            return [category['id'] for category in categories]

        def getActiveProductsByCategoryAlias(self, categoryAlias):
            return self.repository.getActiveProductsByCategoryAlias(categoryAlias)