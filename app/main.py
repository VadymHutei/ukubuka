from flask import Flask

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