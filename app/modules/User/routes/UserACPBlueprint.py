from flask import Blueprint, request
from modules.Language.requestDecorators import language_redirect
from modules.Session.requestDecorators import with_session
from modules.User.controllers.ACPUserController import ACPUserController

ACP_user_blueprint = Blueprint('ACP_user_Blueprint', __name__, url_prefix='/<string:language>/acp/users')
ACP_user_controller = ACPUserController()


@ACP_user_blueprint.route('', methods=['GET'])
@language_redirect
@with_session
def ACP_users_route():
    return ACP_user_controller.users_page_action()


@ACP_user_blueprint.route('/edit', methods=['GET', 'POST'])
@language_redirect
@with_session
def ACP_edit_user_route():
    if request.method == 'GET':
        return ACP_user_controller.edit_user_page_action()
    elif request.method == 'POST':
        return ACP_user_controller.edit_user_action()


@ACP_user_blueprint.route('/block', methods=['GET'])
@language_redirect
@with_session
def block_user_ACP_route():
    return ACP_user_controller.block_user_action()


@ACP_user_blueprint.route('/unblock', methods=['GET'])
@language_redirect
@with_session
def unblock_user_ACP_route():
    return ACP_user_controller.unblock_user_action()


@ACP_user_blueprint.route('/delete', methods=['GET'])
@language_redirect
@with_session
def delete_user_ACP_route():
    return ACP_user_controller.deleteUserAction()
