class ProductController:

    def __init__(self, service, view):
        self.service = service
        self.view = view

    def productAction(self):
        product = self.service.getProduct()
        self.view.addData({'product': product.toArray()})
        return self.view.render()