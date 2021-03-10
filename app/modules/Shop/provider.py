from modules.Shop.controller.ShopController import ShopController
from modules.Shop.repository.ShopRepository import ShopRepository
from modules.Shop.service.ShopService import ShopService
from modules.Shop.view.ShopView import ShopView
from modules.Shop.view.CatalogView import CatalogView
from modules.Shop.view.ProductView import ProductView
from modules.Shop.validator import ShopValidator


class ShopProvider:

    @staticmethod
    def getResources():
        return {
            ShopController: (ShopService, ShopView, CatalogView, ProductView),
            ShopService: (ShopRepository,),
            ShopRepository: (),
            ShopView: ('modules/shop/page.html',),
            CatalogView: ('modules/shop/catalog/page.html',),
            ProductView: ('modules/shop/product/page.html',),
            ShopValidator: ()
        }