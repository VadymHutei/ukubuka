from flask import Blueprint, request

from modules.Language.requestDecorators import languageRedirect
from modules.Session.requestDecorators import withSession
from modules.User.controllers.UserACPController import UserACPController


userACPBlueprint = Blueprint('userACPBlueprint', __name__, url_prefix='/<string:language>/acp/users')
userACPController = UserACPController()

@userACPBlueprint.route('', methods=['GET'])
@languageRedirect
@withSession
def usersACPRoute():
    return userACPController.usersPageAction()

@userACPBlueprint.route('/edit', methods=['GET', 'POST'])
@languageRedirect
@withSession
def editUserACPRoute():
    if request.method == 'GET':
        return userACPController.editUserPageAction()
    elif request.method == 'POST':
        return userACPController.editUserAction()

@userACPBlueprint.route('/block', methods=['GET'])
@languageRedirect
@withSession
def blockUserACPRoute():
    return userACPController.blockUserAction()

@userACPBlueprint.route('/unblock', methods=['GET'])
@languageRedirect
@withSession
def unblockUserACPRoute():
    return userACPController.unblockUserAction()

@userACPBlueprint.route('/delete', methods=['GET'])
@languageRedirect
@withSession
def deleteUserACPRoute():
    return userACPController.deleteUserAction()