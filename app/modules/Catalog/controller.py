class CatalogController:

    def __init__(self, service, view):
        self.service = service
        self.view = view

    def catalogAction(self):
        products = self.service.getProducts()
        self.view.addData({'products': products})
        return self.view.render()