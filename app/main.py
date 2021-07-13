from flask import Flask, request, redirect, url_for, current_app

from modules.Language.service import LanguageService
from modules.Session.service import SessionService
from modules.Home.controller import HomeController
from modules.User.controller import UserController
from modules.User.service import UserService
from modules.Session.request_decorators import withSession
from modules.User.request_decorators import onlyRegistered


app = Flask(__name__)

with app.app_context():
    current_app.languageService = LanguageService()

@app.before_request
def ctx():
    request.ctx = {}

languageService = LanguageService()
sessionService = SessionService()

app.jinja_env.filters['translate'] = languageService.translate


@app.route('/', methods=['GET'])
@withSession
def mainRedirect():
    return redirect(url_for('homePage', language=languageService.defaultLanguage['code']))

@app.route('/<string:language>/', methods=['GET'])
@app.languageService.languageRedirect()
@withSession
def homePage():
    controller = HomeController()
    return controller.homeAction()

@app.route('/<string:language>/registration', methods=['GET', 'POST'])
@app.languageService.languageRedirect()
@withSession
def registration():
    controller = UserController()
    if request.method == 'GET':
        return controller.registrationPageAction()
    elif request.method == 'POST':
        return controller.registrationAction()

@app.route('/<string:language>/login', methods=['GET', 'POST'])
@app.languageService.languageRedirect()
@withSession
def login():
    controller = UserController()
    if request.method == 'GET':
        return controller.loginPageAction()
    elif request.method == 'POST':
        return controller.loginAction()

@app.route('/<string:language>/logout', methods=['GET'])
@app.languageService.languageRedirect()
@withSession
def logout():
    userService = UserService()
    userService.logoutBySessionID(request.ctx['sessionID'])
    return redirect(url_for('homePage', language=request.ctx['language']))

@app.route('/<string:language>/account', methods=['GET'])
@app.languageService.languageRedirect()
@withSession
@onlyRegistered
def account():
    controller = UserController()
    return controller.accountAction()

@app.route('/<string:language>/catalog', methods=['GET'])
@app.languageService.languageRedirect()
def catalogPage():
    controller = CatalogController()
    return controller.catalogAction()

@app.route('/product/<productID>', methods=['GET'])
@app.languageService.languageRedirect()
def productPage(productID):
    controller = ProductController()
    return controller.productAction(productID)

@app.route('/<string:language>/shop', methods=['GET'])
@app.languageService.languageRedirect()
def shopPage(language):
    controller = ShopController()
    return controller.shopAction()

@app.route('/<string:language>/shop/<path:path>', methods=['GET'])
@app.languageService.languageRedirect()
def shop(language, path):
    controller = ShopController()
    return controller.shopAction(path)

# ACP
@app.route('/<string:language>/acp', methods=['GET'])
@app.languageService.languageRedirect()
def acpPage(language):
    controller = ACPController()
    return controller.ACPAction(language)

@app.route('/<string:language>/acp/translates', methods=['GET'])
@app.languageService.languageRedirect()
def acpTranslatesPage(language):
    controller = ACPController()
    return controller.translatesAction(language, request.args.get('for_language', language))

@app.route('/<string:language>/acp/categories', methods=['GET'])
@app.languageService.languageRedirect()
def acpCategories(language):
    controller = ACPController()
    return controller.categoriesAction()