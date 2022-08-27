from flask import Blueprint, request, redirect, url_for

from modules.Language.requestDecorators import languageRedirect
from modules.Session.requestDecorators import withSession
from modules.User.controllers.UserController import UserController
from modules.User.requestDecorators import onlyRegistered
from modules.User.services.UserService import UserService


userBlueprint = Blueprint('userBlueprint', __name__)
controller = UserController()


@userBlueprint.route('/<string:language>/registration', methods=['GET', 'POST'])
@languageRedirect
@withSession
def registrationRoute():
    if request.method == 'GET':
        return controller.registrationPageAction()
    elif request.method == 'POST':
        return controller.registrationAction()


@userBlueprint.route('/<string:language>/login', methods=['GET', 'POST'])
@languageRedirect
@withSession
def loginRoute():
    if request.method == 'GET':
        return controller.loginPageAction()
    elif request.method == 'POST':
        return controller.loginAction()


@userBlueprint.route('/<string:language>/logout', methods=['GET'])
@languageRedirect
@withSession
def logoutRoute():
    userService = UserService()
    userService.logout_by_session_ID(request.ctx['sessionID'])
    return redirect(url_for('homeBlueprint.homeRoute', language=request.ctx['language'].code))


@userBlueprint.route('/<string:language>/account', methods=['GET'])
@languageRedirect
@withSession
@onlyRegistered
def accountRoute():
    return controller.accountAction()
