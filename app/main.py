from flask import Flask, g, url_for, redirect

from blueprints import blueprints_list
from blueprints.ACP.DashboardACPBlueprint import acp_dashboard_blueprint
from blueprints.ACP.LanguageBlueprint import acp_language_blueprint
from blueprints.blueprint_names import HOME_BLUEPRINT
from blueprints.website.CatalogBlueprint import catalog_blueprint
from blueprints.website.ProductBlueprint import product_blueprint
from modules.Category.routes.CategoryACPBlueprint import categoryACPBlueprint
from modules.Language.jinjaFilters import filters as language_filters
from modules.Language.routes.TranslationsACPBlueprint import translationsACPBlueprint
from modules.Session.requestDecorators import with_session
from modules.User.routes.UserACPBlueprint import ACP_user_blueprint
from modules.User.routes.UserBlueprint import user_blueprint
from service_container import sc
from services.Config.ConfigService import ConfigService
from services.Language.LanguageService import LanguageService

app = Flask(__name__, instance_relative_config=True)

app.config.from_object('config')
app.config.from_pyfile('config.py')
app.jinja_env.filters.update(language_filters)


@app.before_request
def before_request() -> None:
    if ConfigService.APP_CONFIG_KEY not in app.config or app.config[ConfigService.APP_CONFIG_KEY] is False:
        config_service: ConfigService = sc.get(ConfigService)
        config: dict = config_service.get_config()
        app.config.update(config)
        app.config[ConfigService.APP_CONFIG_KEY] = True

    language_service: LanguageService = sc.get(LanguageService)
    app.config['AVAILABLE_LANGUAGE_CODES'] = [language.code for language in language_service.find_active()]
    g.default_language = language_service.get_by_code(app.config['default_language_code'])


for blueprint in blueprints_list:
    app.register_blueprint(blueprint)


@app.route('/', methods=['GET'])
@with_session
def language_redirect():
    home_route = '.'.join((HOME_BLUEPRINT, 'home_route'))
    url = url_for(home_route, language_code=g.default_language.code)

    return redirect(url)


app.register_blueprint(catalog_blueprint)
app.register_blueprint(categoryACPBlueprint)
app.register_blueprint(product_blueprint)
app.register_blueprint(translationsACPBlueprint)
app.register_blueprint(user_blueprint)

app.register_blueprint(acp_dashboard_blueprint)
app.register_blueprint(acp_language_blueprint)
app.register_blueprint(ACP_user_blueprint)
