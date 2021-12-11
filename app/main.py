from flask import Flask, redirect, request, url_for

from modules.Catalog.controller import CatalogController
from modules.ACP.controllers.ACPController import ACPController
from modules.Home.controller import HomeController
from modules.Language.controllers.ACPTranslationController import ACPTranslationController
from modules.Language.requestDecorators import languageRedirect
from modules.Language.services.LanguageService import LanguageService
from modules.Session.requestDecorators import withSession
from modules.User.controllers.UserACPController import UserACPController
from modules.User.controllers.UserController import UserController
from modules.User.requestDecorators import onlyRegistered
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


@app.route('/', methods=['GET'])
@withSession
def mainRedirect():
    return redirect(url_for('homePage', language=app.languageService.defaultLanguage.code))

@app.route('/<string:language>/', methods=['GET'])
@languageRedirect
@withSession
def homePage():
    controller = HomeController()
    return controller.homeAction()

@app.route('/<string:language>/registration', methods=['GET', 'POST'])
@languageRedirect
@withSession
def registration():
    controller = UserController()
    if request.method == 'GET':
        return controller.registrationPageAction()
    elif request.method == 'POST':
        return controller.registrationAction()

@app.route('/<string:language>/login', methods=['GET', 'POST'])
@languageRedirect
@withSession
def login():
    controller = UserController()
    if request.method == 'GET':
        return controller.loginPageAction()
    elif request.method == 'POST':
        return controller.loginAction()

@app.route('/<string:language>/logout', methods=['GET'])
@languageRedirect
@withSession
def logout():
    userService = UserService()
    userService.logoutBySessionID(request.ctx['sessionID'])
    return redirect(url_for('homePage', language=request.ctx['language']))

@app.route('/<string:language>/account', methods=['GET'])
@languageRedirect
@withSession
@onlyRegistered
def account():
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
def ACPDashboardPage():
    controller = ACPController()
    return controller.dashboardAction()

@app.route('/<string:language>/acp/translations', methods=['GET'])
@languageRedirect
def ACPTranslationPage():
    controller = ACPTranslationController()
    return controller.listAction()

@app.route('/<string:language>/acp/translations/edit', methods=['GET', 'POST'])
@languageRedirect
def ACPTranslationEditPage():
    controller = ACPTranslationController()
    if request.method == 'GET':
        return controller.editPageAction()
    elif request.method == 'POST':
        return controller.editAction()

@app.route('/<string:language>/acp/users', methods=['GET'])
@languageRedirect
def usersListACP():
    controller = UserACPController()
    return controller.usersListAction()

@app.route('/<string:language>/acp/users/edit', methods=['GET'])
@languageRedirect
def editUserACProute():
    controller = UserACPController()
    return controller.usersListAction()

@app.route('/<string:language>/acp/users/block', methods=['GET'])
@languageRedirect
def blockUserACProute():
    controller = UserACPController()
    return controller.usersListAction()

@app.route('/<string:language>/acp/users/delete', methods=['GET'])
@languageRedirect
def deleteUserACProute():
    controller = UserACPController()
    return controller.usersListAction()