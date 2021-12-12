from flask import Flask, redirect, request, url_for

from modules.ACP.controllers.ACPController import ACPController
from modules.Home.routes.HomeBlueprint import homeBlueprint
from modules.Language.requestDecorators import languageRedirect
from modules.Language.routes.TranslationsACPBlueprint import translationsACPBlueprint
from modules.Language.services.LanguageService import LanguageService
from modules.User.routes.UserACPBlueprint import userACPBlueprint
from modules.User.routes.UserBlueprint import userBlueprint
from vendor.ukubuka.JinjaFilters import viewJinjaFilter


app = Flask(__name__)

app.languageService = LanguageService()

app.jinja_env.filters['translate'] = app.languageService.translate
app.jinja_env.filters['pathWithLanguage'] = app.languageService.pathWithLanguage
app.jinja_env.filters['view'] = viewJinjaFilter

@app.before_request
def ctx():
    request.ctx = {}

app.register_blueprint(homeBlueprint)
app.register_blueprint(translationsACPBlueprint)
app.register_blueprint(userACPBlueprint)
app.register_blueprint(userBlueprint)

# @app.route('/<string:language>/catalog', methods=['GET'])
# @languageRedirect
# @withSession
# def catalogMainPage():
#     controller = CatalogController()
#     return controller.catalogMainPageAction()

# @app.route('/<string:language>/catalog/<string:catalogAlias>', methods=['GET'])
# @languageRedirect
# @withSession
# def catalogPage(catalogAlias):
#     controller = CatalogController()
#     return controller.catalogAction(catalogAlias)

# @app.route('/product/<productID>', methods=['GET'])
# @languageRedirect
# def productPage(productID):
#     controller = ProductController()
#     return controller.productAction(productID)

# @app.route('/<string:language>/shop', methods=['GET'])
# @languageRedirect
# def shopPage():
#     controller = ShopController()
#     return controller.shopAction()

# @app.route('/<string:language>/shop/<path:path>', methods=['GET'])
# @languageRedirect
# def shop(path):
#     controller = ShopController()
#     return controller.shopAction(path)

# ACP
@app.route('/<string:language>/acp', methods=['GET'])
@languageRedirect
def dashboardACPRoute():
    print(request.blueprint)
    controller = ACPController()
    return controller.dashboardAction()