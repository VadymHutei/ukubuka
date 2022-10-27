from flask import Blueprint, g, redirect, request, url_for
from modules.Language.requestDecorators import language_redirect
from modules.Session.requestDecorators import with_session
from modules.User.controllers.UserController import UserController
from modules.User.requestDecorators import onlyRegistered
from modules.User.services.UserService import UserService

user_blueprint = Blueprint('user_blueprint', __name__)
controller = UserController()


@user_blueprint.route('/<string:language>/registration', methods=['GET', 'POST'])  # type: ignore
@language_redirect
@with_session
def registration_route():
    if request.method == 'GET':
        return controller.registration_page_action()
    elif request.method == 'POST':
        return controller.registration_action()


@user_blueprint.route('/<string:language>/login', methods=['GET', 'POST'])  # type: ignore
@language_redirect
@with_session
def login_route():
    if request.method == 'GET':
        return controller.loginPageAction()
    elif request.method == 'POST':
        return controller.loginAction()


@user_blueprint.route('/<string:language>/logout', methods=['GET'])
@language_redirect
@with_session
def logout_route():
    userService = UserService()
    userService.logout_by_session_ID(g.session_ID)
    return redirect(url_for('home_blueprint.home_route', language=g.current_language.code))


@user_blueprint.route('/<string:language>/account', methods=['GET'])
@language_redirect
@with_session
@onlyRegistered
def account_route():
    return controller.account_action()
