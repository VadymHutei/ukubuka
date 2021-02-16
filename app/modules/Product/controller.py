from ukubuka.AbstractController import AbstractController


class ProductController(AbstractController):

    def __init__(self, service, view):
        self.service = service
        self.view = view

    def productAction(self, productID):
        product = self.service.getProductByID(productID)
        self.view.addData({'product': product})
        return self.view.render()