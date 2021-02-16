from ukubuka.AbstractService import AbstractService
from modules.Product.entity import ProductEntity


class ProductService(AbstractService):

    def __init__(self, repository):
        self.repository = repository

    def getProductByID(self, productID):
        product = self.repository.getProductByID(productID)
        return ProductEntity(product)