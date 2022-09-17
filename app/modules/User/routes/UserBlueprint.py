from flask import Blueprint, redirect, request, url_for
from modules.Language.requestDecorators import language_redirect
from modules.Session.requestDecorators import with_session
from modules.User.controllers.UserController import UserController
from modules.User.requestDecorators import onlyRegistered
from modules.User.services.UserService import UserService

userBlueprint = Blueprint('userBlueprint', __name__)
controller = UserController()


@userBlueprint.route('/<string:language>/registration', methods=['GET', 'POST'])
@language_redirect
@with_session
def registrationRoute():
    if request.method == 'GET':
        return controller.registrationPageAction()
    elif request.method == 'POST':
        return controller.registrationAction()


@userBlueprint.route('/<string:language>/login', methods=['GET', 'POST'])
@language_redirect
@with_session
def loginRoute():
    if request.method == 'GET':
        return controller.loginPageAction()
    elif request.method == 'POST':
        return controller.loginAction()


@userBlueprint.route('/<string:language>/logout', methods=['GET'])
@language_redirect
@with_session
def logoutRoute():
    userService = UserService()
    userService.logout_by_session_ID(g.session_ID)
    return redirect(url_for('homeBlueprint.homeRoute', language=g.current_language.code))


@userBlueprint.route('/<string:language>/account', methods=['GET'])
@language_redirect
@with_session
@onlyRegistered
def accountRoute():
    return controller.accountAction()
