from flask import Flask, abort

from container import Container
from language import langRedirect


app = Flask(__name__)
container = Container()


@app.route('/', methods=['GET'])
@langRedirect
def homePage():
    controller = container.get('HomePageController')
    return controller.homePageAction()

@app.route('/catalog', methods=['GET'])
@langRedirect
def catalogPage():
    controller = container.get('CatalogController')
    return controller.catalogAction()

@app.route('/product/<productID>', methods=['GET'])
@langRedirect
def productPage(productID):
    controller = container.get('ProductController')
    return controller.productAction(productID)

@app.route('/<string:language>/shop', methods=['GET'])
@langRedirect
def shopPage(language):
    controller = container.get('ShopController')
    return controller.shopAction()

@app.route('/<string:language>/shop/<path:path>', methods=['GET'])
@langRedirect
def shop(language, path):
    controller = container.get('ShopController')
    return controller.shopAction(path)