from flask import Flask, g, request

from jinjaFilters import filters
from modules.ACP.routes.DashboardACPBlueprint import dashboardACPBlueprint
from modules.Category.routes.CategoryACPBlueprint import categoryACPBlueprint
from modules.Home.routes.HomeBlueprint import homeBlueprint
from modules.Language.routes.TranslationsACPBlueprint import translationsACPBlueprint
from modules.Language.Translator import Translator
from modules.User.routes.UserACPBlueprint import userACPBlueprint
from modules.User.routes.UserBlueprint import userBlueprint

app = Flask(__name__, instance_relative_config=True)

app.config.from_object("config")
app.config.from_pyfile("config.py")

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
