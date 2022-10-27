from flask import Flask, g

from modules.ACP.routes.DashboardACPBlueprint import dashboardACPBlueprint
from modules.Category.routes.CategoryACPBlueprint import categoryACPBlueprint
from modules.Home.routes.HomeBlueprint import home_blueprint
from modules.Language.jinjaFilters import filters as language_filters
from modules.Language.routes.TranslationsACPBlueprint import translationsACPBlueprint
from modules.Language.Translator import Translator
from modules.User.routes.UserACPBlueprint import ACP_user_blueprint
from modules.User.routes.UserBlueprint import user_blueprint

app = Flask(__name__, instance_relative_config=True)

app.config.from_object("config")
app.config.from_pyfile("config.py")


app.jinja_env.filters.update(language_filters)


@app.before_request
def before_request() -> None:
    g.t = Translator.getInstance()
    g.current_language = g.t.default_language


app.register_blueprint(home_blueprint)
app.register_blueprint(user_blueprint)
app.register_blueprint(categoryACPBlueprint)
app.register_blueprint(dashboardACPBlueprint)
app.register_blueprint(translationsACPBlueprint)
app.register_blueprint(ACP_user_blueprint)
