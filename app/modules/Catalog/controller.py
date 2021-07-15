from modules.Ukubuka.view import UkubukaView
from modules.Catalog.service import CatalogService

class CatalogController():

    def __init__(self):
        self.service = CatalogService()
        self.view = UkubukaView('modules/Catalog/catalog.html')

    def catalogAction(self):
        catalogAlias = 'flowers'
        catalog = self.service.getCatalogByAlias(categoryAlias)
        products = self.service.getProductsByCatalogID(catalog['id'])
        self.view.addData({
            'catalog': catalog,
            'products': products,
        })
        return self.view.render()