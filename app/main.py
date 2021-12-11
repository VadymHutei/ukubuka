from flask import redirect, request, url_for

from app import app

from modules.ACP.controllers.ACPController import ACPController
from modules.Home.controller import HomeController
from modules.Language.controllers.TranslationACPController import TranslationACPController
from modules.Language.requestDecorators import languageRedirect
from modules.Session.requestDecorators import withSession
from modules.User.controllers.UserACPController import UserACPController
from modules.User.controllers.UserController import UserController
from modules.User.requestDecorators import onlyRegistered
from modules.User.services.UserService import UserService


@app.route('/', methods=['GET'])
@withSession
def mainRedirect():
    return redirect(url_for('homeRoute', language=app.languageService.defaultLanguage.code))

@app.route('/<string:language>/', methods=['GET'])
@languageRedirect
@withSession
def homeRoute():
    controller = HomeController()
    return controller.homeAction()

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

@app.route('/<string:language>/acp/translations', methods=['GET'])
@languageRedirect
def translationsACPRoute():
    controller = TranslationACPController()
    return controller.translationsAction()

@app.route('/<string:language>/acp/translations/edit', methods=['GET', 'POST'])
@languageRedirect
def editTranslationACPRoute():
    controller = TranslationACPController()
    if request.method == 'GET':
        return controller.editPageAction()
    elif request.method == 'POST':
        return controller.editAction()
    return controller.translationsAction()

@app.route('/<string:language>/acp/translations/delete', methods=['GET', 'POST'])
@languageRedirect
def deleteTranslationACPRoute():
    controller = TranslationACPController()
    if request.method == 'GET':
        return controller.deletePageAction()
    elif request.method == 'POST':
        return controller.deleteAction()

@app.route('/<string:language>/acp/users', methods=['GET'])
@languageRedirect
def usersACPRoute():
    controller = UserACPController()
    return controller.usersAction()

@app.route('/<string:language>/acp/users/edit', methods=['GET'])
@languageRedirect
def editUserACProute():
    controller = UserACPController()
    return controller.usersAction()

@app.route('/<string:language>/acp/users/block', methods=['GET'])
@languageRedirect
def blockUserACProute():
    controller = UserACPController()
    return controller.usersAction()

@app.route('/<string:language>/acp/users/delete', methods=['GET'])
@languageRedirect
def deleteUserACProute():
    controller = UserACPController()
    return controller.usersAction()