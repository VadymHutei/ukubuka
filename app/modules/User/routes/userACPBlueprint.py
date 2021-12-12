from flask import Blueprint

from modules.Language.requestDecorators import languageRedirect
from modules.Session.requestDecorators import withSession
from modules.User.controllers.UserACPController import UserACPController


userACPBlueprint = Blueprint('userACPBlueprint', __name__, url_prefix='/<string:language>/acp/users')
controller = UserACPController()

@userACPBlueprint.route('', methods=['GET'])
@languageRedirect
@withSession
def usersACPRoute():
    return controller.usersAction()

@userACPBlueprint.route('/edit', methods=['GET'])
@languageRedirect
@withSession
def editUserACPRoute():
    return controller.usersAction()

@userACPBlueprint.route('/block', methods=['GET'])
@languageRedirect
@withSession
def blockUserACPRoute():
    return controller.usersAction()

@userACPBlueprint.route('/delete', methods=['GET'])
@languageRedirect
@withSession
def deleteUserACPRoute():
    return controller.usersAction()