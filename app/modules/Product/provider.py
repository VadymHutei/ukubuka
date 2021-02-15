from modules.Product.controller import ProductController
from modules.Product.service import ProductService
from modules.Product.repository import ProductRepository
from modules.Product.view import ProductView


class ProductProvider:

    @staticmethod
    def getResources():
        return {
            ProductController: (ProductService, ProductView),
            ProductService: (ProductRepository,),
            ProductRepository: (),
            ProductView: ('modules/product/page.html',)
        }