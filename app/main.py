from flask import Flask, abort

from container import Container


app = Flask(__name__)
container = Container()

@app.route('/', methods=['GET'])
def homePage():
    controller = container.get('HomePageController')
    return controller.homePageAction()

@app.route('/catalog', methods=['GET'])
def catalogPage():
    controller = container.get('CatalogController')
    return controller.catalogAction()

@app.route('/product/<productID>', methods=['GET'])
def productPage(productID):
    controller = container.get('ProductController')
    return controller.productAction(productID)

@app.route('/shop', methods=['GET'])
def shopPage():
    controller = container.get('ShopController')
    return controller.shopAction()

@app.route('/shop/<path:path>', methods=['GET'])
def shop(path):
    shopPathResolver = container.get('ShopPathResolver')
    requestedResource = shopPathResolver.resolve(path)
    if not requestedResource.isValidPath:
        abort(404)
    controller = container.get('ShopController')
    if requestedResource.isCatalog:
        return controller.catalogAction(requestedResource.identifierType())