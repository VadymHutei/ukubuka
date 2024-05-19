from flask import Blueprint, g, redirect, url_for

from blueprints.blueprint_names import HOME_BLUEPRINT
from modules.Home.controllers.HomeController import HomeController
from modules.Session.requestDecorators import with_session
from request_decorators import with_language

home_blueprint = Blueprint(HOME_BLUEPRINT, __name__)

@home_blueprint.route('/', methods=['GET'])
@with_session
def main_redirect():
    home_route = '.'.join((HOME_BLUEPRINT, 'home_route'))
    url = url_for(home_route, language=g.t.default_language.code)

    return redirect(url)

@home_blueprint.route('/<string:language>/', methods=['GET'])
@with_language
@with_session
def home_route():
    controller = HomeController()
    return controller.home_action()