from flask import Flask, abort

from container import Container


app = Flask(__name__)

container = Container()
languageService = container.get('LanguageService')
app.jinja_env.filters['translate'] = languageService.translate


# Shop
@app.route('/', methods=['GET'])
@languageService.langRedirect()
def homePage():
    controller = container.get('HomePageController')
    return controller.homePageAction()

@app.route('/catalog', methods=['GET'])
@languageService.langRedirect()
def catalogPage():
    controller = container.get('CatalogController')
    return controller.catalogAction()

@app.route('/product/<productID>', methods=['GET'])
@languageService.langRedirect()
def productPage(productID):
    controller = container.get('ProductController')
    return controller.productAction(productID)

@app.route('/<string:language>/shop', methods=['GET'])
@languageService.langRedirect()
def shopPage(language):
    controller = container.get('ShopController')
    return controller.shopAction()

@app.route('/<string:language>/shop/<path:path>', methods=['GET'])
@languageService.langRedirect()
def shop(language, path):
    controller = container.get('ShopController')
    return controller.shopAction(path)

# ACP
@app.route('/<string:language>/acp', methods=['GET'])
@languageService.langRedirect()
def acpPage(language):
    controller = container.get('ACPController')
    return controller.ACPAction(language)

@app.route('/<string:language>/acp/categories', methods=['GET'])
@languageService.langRedirect()
def acpCategories(language):
    controller = container.get('ACPController')
    return controller.categoriesAction()