from flask import Flask, redirect, request, url_for

from modules.ACP.controllers.ACPController import ACPController
from modules.Home.routes.HomeBlueprint import homeBlueprint
from modules.Language.requestDecorators import languageRedirect
from modules.Language.routes.translationsACPBlueprint import translationsACPBlueprint
from modules.Language.services.LanguageService import LanguageService
from modules.Session.requestDecorators import withSession
from modules.User.controllers.UserController import UserController
from modules.User.requestDecorators import onlyRegistered
from modules.User.routes.userACPBlueprint import userACPBlueprint
from modules.User.services.UserService import UserService
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

@app.route('/<string:language>/registration', methods=['GET', 'POST'])
@languageRedirect
@withSession
def registrationRoute():
    controller = UserController()
    if request.method == 'GET':
        return controller.registrationPageAction()
    elif request.method == 'POST':
        return controller.registrationAction()

@app.route('/<string:language>/login', methods=['GET', 'POST'])
@languageRedirect
@withSession
def loginRoute():
    controller = UserController()
    if request.method == 'GET':
        return controller.loginPageAction()
    elif request.method == 'POST':
        return controller.loginAction()

@app.route('/<string:language>/logout', methods=['GET'])
@languageRedirect
@withSession
def logoutRoute():
    userService = UserService()
    userService.logoutBySessionID(request.ctx['sessionID'])
    return redirect(url_for('homeRoute', language=request.ctx['language']))

@app.route('/<string:language>/account', methods=['GET'])
@languageRedirect
@withSession
@onlyRegistered
def accountRoute():
    controller = UserController()
    return controller.accountAction()

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
    controller = ACPController()
    return controller.dashboardAction()