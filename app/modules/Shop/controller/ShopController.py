from flask import abort

from ukubuka.AbstractController import AbstractController


class ShopController(AbstractController):

    def __init__(self, repository, shopView, catalogView, productView):
        self._repository = repository
        self._shopView = shopView
        self._catalogView = catalogView
        self._productView = productView

    def shopAction(self):
        return self._shopView.render()

    def catalogAction(self, catalogID=None, catalogAlias=None):
        if catalogID is not None:
            catalog = self.repository.getCatalogById(catalogID)
        elif catalogAlias is not None:
            catalog = self.repository.getCatalogByAlias(catalogAlias)
        else:
            raise Exception('catalogID or catalogAlias are required in catalogAction')
        if not catalog:
            abort(404)
        self._catalogView.addData({'catalog': catalog})
        return self._catalogView.render()