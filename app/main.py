from flask import Flask, request, redirect, url_for

from modules.Language.service import LanguageService
from modules.Session.service import SessionService
from modules.Home.controller import HomeController
from modules.User.controller import UserController


app = Flask(__name__)

@app.before_request
def cnx():
    request.cnx = {}

languageService = LanguageService()
sessionService = SessionService()

app.jinja_env.filters['translate'] = languageService.translate


@app.route('/', methods=['GET'])
@sessionService.withSession()
def mainRedirect():
    return redirect(url_for('homePage', language=languageService.defaultLanguage['code']))

@app.route('/<string:language>/', methods=['GET'])
@languageService.languageRedirect()
@sessionService.withSession()
def homePage():
    controller = HomeController()
    return controller.homeAction()

@app.route('/<string:language>/registration', methods=['GET', 'POST'])
@languageService.languageRedirect()
@sessionService.withSession()
def registration():
    controller = UserController()
    if request.method == 'GET':
        return controller.registrationPageAction()
    elif request.method == 'POST':
        return controller.registrationAction()

@app.route('/<string:language>/login', methods=['GET', 'POST'])
@languageService.languageRedirect()
@sessionService.withSession()
def login():
    controller = UserController()
    if request.method == 'GET':
        return controller.loginPageAction()
    elif request.method == 'POST':
        return controller.loginAction()

@app.route('/<string:language>/catalog', methods=['GET'])
@languageService.languageRedirect()
def catalogPage():
    controller = CatalogController()
    return controller.catalogAction()

@app.route('/product/<productID>', methods=['GET'])
@languageService.languageRedirect()
def productPage(productID):
    controller = ProductController()
    return controller.productAction(productID)

@app.route('/<string:language>/shop', methods=['GET'])
@languageService.languageRedirect()
def shopPage(language):
    controller = ShopController()
    return controller.shopAction()

@app.route('/<string:language>/shop/<path:path>', methods=['GET'])
@languageService.languageRedirect()
def shop(language, path):
    controller = ShopController()
    return controller.shopAction(path)

# ACP
@app.route('/<string:language>/acp', methods=['GET'])
@languageService.languageRedirect()
def acpPage(language):
    controller = ACPController()
    return controller.ACPAction(language)

@app.route('/<string:language>/acp/translates', methods=['GET'])
@languageService.languageRedirect()
def acpTranslatesPage(language):
    controller = ACPController()
    return controller.translatesAction(language, request.args.get('for_language', language))

@app.route('/<string:language>/acp/categories', methods=['GET'])
@languageService.languageRedirect()
def acpCategories(language):
    controller = ACPController()
    return controller.categoriesAction()