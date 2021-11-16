from flask import abort

from modules.Ukubuka.UkubukaView import UkubukaView
from modules.Catalog.service import CatalogService

class CatalogController:

    def __init__(self):
        self.service = CatalogService()

    def catalogMainPageAction(self):
        catalogs = self.service.getActiveCatalogs()
        view = UkubukaView('modules/Catalog/catalog_main_page.html')
        view.addData({
            'catalogs': catalogs,
        })
        return view.render()

    def catalogAction(self, catalogAlias):
        catalog = self.service.getCatalogByAlias(catalogAlias)
        if catalog is None:
            abort(404)
        products = self.service.getProductsByCatalogID(catalog['id'])
        view = UkubukaView('modules/Catalog/catalog.html')
        view.addData({
            'catalog': catalog,
            'products': products,
        })
        return view.render()