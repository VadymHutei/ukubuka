from flask import Blueprint

from blueprints.blueprint_names import HOME_BLUEPRINT
from modules.Home.controllers.HomeController import HomeController
from modules.Session.requestDecorators import with_session
from request_decorators import with_language
from service_container import sc

home_blueprint = Blueprint(HOME_BLUEPRINT, __name__, url_prefix='/<string:language_code>')


@home_blueprint.route('', methods=['GET'])
@with_language
@with_session
def home_route():
    controller: HomeController = sc.get(HomeController)

    return controller.home_page_action()
