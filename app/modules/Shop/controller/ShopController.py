from flask import abort

from ukubuka.AbstractController import AbstractController
from modules.Shop.validator import ShopValidator


class ShopController(AbstractController):

    CATALOG_TYPE = 'catalog'
    CATEGORY_TYPE = 'category'
    PRODUCT_TYPE = 'product'
    SKU_TYPE = 'SKU'

    def __init__(self, service, shopView, catalogView, productView):
        self._service = service
        self._shopView = shopView
        self._catalogView = catalogView
        self._productView = productView

    def shopAction(self, path=None):
        if path is None:
            return self._shopView.render()

        isValidPath, resourceType, resourceID = self._resolvePath(path)

        if not isValidPath:
            abort(404)

        if resourceType == self.CATALOG_TYPE:
            return self.catalogAction(resourceID)
        elif resourceType == self.CATEGORY_TYPE:
            return self.categoryAction(resourceID)
        elif resourceType == self.PRODUCT_TYPE:
            return self.productAction(resourceID)
        elif resourceType == self.SKU_TYPE:
            return self.SKUAction(resourceID)

    def catalogAction(self, catalogID):
        catalog = self._service.getCatalogByID(catalogID)
        self._catalogView.addData({'catalog': catalog})
        return self._catalogView.render()

    def categoryAction(self, categoryID):
        category = self._service.getCategoryByID(categoryID)
        self._catalogView.addData({'category': category})
        return self._catalogView.render()

    def productAction(self, productID):
        product = self._service.getProductByID(productID)
        self._productView.addData({'product': product})
        return self._productView.render()

    def SKUAction(self, SKUID):
        SKU = self._service.getSKUByID(SKUID)
        self._productView.addData({'SKU': SKU})
        return self._productView.render()

    def _resolvePath(self, path):
        path = path.split('/')
        lastSegment = path[-1]

        if ShopValidator.catalogID(lastSegment):
            data = self._service.getCatalogByID(lastSegment)
            if data:
                return True, self.CATALOG_TYPE, data['id']
        if ShopValidator.catalogAlias(lastSegment):
            data = self._service.getCatalogByAlias(lastSegment)
            if data:
                return True, self.CATALOG_TYPE, data['id']
        if ShopValidator.categoryID(lastSegment):
            data = self._service.getCategoryByID(lastSegment)
            if data:
                return True, self.CATEGORY_TYPE, data['id']
        if ShopValidator.categoryAlias(lastSegment):
            data = self._service.getCategoryByAlias(lastSegment)
            if data:
                return True, self.CATEGORY_TYPE, data['id']
        if ShopValidator.productID(lastSegment):
            data = self._service.getProductByID(lastSegment)
            if data:
                return True, self.PRODUCT_TYPE, data['id']
        if ShopValidator.productAlias(lastSegment):
            data = self._service.getProductByAlias(lastSegment)
            if data:
                return True, self.PRODUCT_TYPE, data['id']
        if ShopValidator.SKUID(lastSegment):
            data = self._service.getSKUByID(lastSegment)
            if data:
                return True, self.SKU_TYPE, data['id']
        if ShopValidator.SKUAlias(lastSegment):
            data = self._service.getSKUByAlias(lastSegment)
            if data:
                return True, self.SKU_TYPE, data['id']

        return False, None, None