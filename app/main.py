from flask import Flask, request, g

from jinjaFilters import filters

from modules.ACP.routes.DashboardACPBlueprint import dashboardACPBlueprint
from modules.Category.routes.CategoryACPBlueprint import categoryACPBlueprint
from modules.Home.routes.HomeBlueprint import homeBlueprint
from modules.Language.routes.TranslationsACPBlueprint import translationsACPBlueprint
from modules.Language.Translator import Translator
from modules.User.routes.UserACPBlueprint import userACPBlueprint
from modules.User.routes.UserBlueprint import userBlueprint


app = Flask(__name__)

app.jinja_env.filters.update(filters)

@app.before_request
def beforeRequest():
    request.ctx = {}
    g.t = Translator.getInstance()

app.register_blueprint(homeBlueprint)
app.register_blueprint(userBlueprint)

app.register_blueprint(categoryACPBlueprint)
app.register_blueprint(dashboardACPBlueprint)
app.register_blueprint(translationsACPBlueprint)
app.register_blueprint(userACPBlueprint)

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