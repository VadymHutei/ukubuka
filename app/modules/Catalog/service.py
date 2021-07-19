from modules.Catalog.repository import CatalogRepository
from modules.Category.service import CategoryService


class CatalogService:

    def __init__(self):
        self.repository = CatalogRepository()

    def getActiveCatalogs(self):
        return self.repository.getActiveCatalogs()

    def getCatalogByAlias(self, catalogAlias):
        return self.repository.getCatalogByAlias(catalogAlias)

    def getProductsByCatalogID(self, catalogID):
        categoryService = CategoryService()
        catalogCategoryIDs = self.getCategoryIDsByCatalogID(catalogID)
        categoryIDs = categoryService.getSubcategoryIDs(catalogCategoryIDs)
        catalogProducts = categoryService.getProductsByCategoryIDs(categoryIDs)
        catalogProducts += self.repository.getProductsByCatalogID(catalogID)
        return catalogProducts

    def getCategoryIDsByCatalogID(self, catalogID):
        categories = self.repository.getCategoriesByCatalogID(catalogID)
        return [category['id'] for category in categories]

    def getActiveProductsByCategoryAlias(self, categoryAlias):
        return self.repository.getActiveProductsByCategoryAlias(categoryAlias)