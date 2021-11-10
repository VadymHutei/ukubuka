from flask import Flask, request, redirect, url_for, current_app

from modules.ACP.Dashboard.controller import DashboardController
from modules.ACP.Translations.controller import TranslationsController
from modules.Catalog.controller import CatalogController
from modules.Home.controller import HomeController
from modules.Language.request_decorators import languageRedirect
from modules.Language.service import LanguageService
from modules.Session.request_decorators import withSession
from modules.User.controller import UserController
from modules.User.request_decorators import onlyRegistered
from modules.User.service import UserService


app = Flask(__name__)

app.languageService = LanguageService()
app.jinja_env.filters['translate'] = app.languageService.translate
app.jinja_env.filters['pathWithLanguage'] = app.languageService.pathWithLanguage

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

@app.route('/<string:language>/catalog', methods=['GET'])
@languageRedirect
@withSession
def catalogMainPage():
    controller = CatalogController()
    return controller.catalogMainPageAction()

@app.route('/<string:language>/catalog/<string:catalogAlias>', methods=['GET'])
@languageRedirect
@withSession
def catalogPage(catalogAlias):
    controller = CatalogController()
    return controller.catalogAction(catalogAlias)

@app.route('/product/<productID>', methods=['GET'])
@languageRedirect
def productPage(productID):
    controller = ProductController()
    return controller.productAction(productID)

@app.route('/<string:language>/shop', methods=['GET'])
@languageRedirect
def shopPage():
    controller = ShopController()
    return controller.shopAction()

@app.route('/<string:language>/shop/<path:path>', methods=['GET'])
@languageRedirect
def shop(language, path):
    controller = ShopController()
    return controller.shopAction(path)

# ACP
@app.route('/<string:language>/acp', methods=['GET'])
@languageRedirect
def acpPage():
    controller = DashboardController()
    return controller.dashboardAction()

@app.route('/<string:language>/acp/translations', methods=['GET'])
@languageRedirect
def acpTranslationsPage():
    controller = TranslationsController()
    return controller.listAction()

@app.route('/<string:language>/acp/translations/edit', methods=['GET'])
@languageRedirect
def acpTranslationsEditPage():
    controller = TranslationsController()
    return controller.editAction()

@app.route('/<string:language>/acp/categories', methods=['GET'])
@languageRedirect
def acpCategories():
    controller = ACPController()
    return controller.categoriesAction()