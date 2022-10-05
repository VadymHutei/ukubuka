from flask import Blueprint, g, redirect, url_for
from modules.Home.controllers.HomeController import HomeController
from modules.Language.requestDecorators import language_redirect
from modules.Session.requestDecorators import with_session

home_blueprint = Blueprint('home_blueprint', __name__)


@home_blueprint.route('/', methods=['GET'])
@with_session
def main_redirect():
    return redirect(url_for('home_blueprint.home_route', language=g.t.default_language.code))


@home_blueprint.route('/<string:language>/', methods=['GET'])
@language_redirect
@with_session
def home_route():
    controller = HomeController()
    return controller.home_action()
