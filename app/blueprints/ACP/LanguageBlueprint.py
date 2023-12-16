from flask import Blueprint, request

from blueprints.blueprint_names import ACP_LANGUAGE_BLUEPRINT
from controllers.ACP.LanguageController import LanguageController
from modules.Session.requestDecorators import with_session
from request_decorators import with_language
from service_container import sc

acp_language_blueprint = Blueprint(ACP_LANGUAGE_BLUEPRINT, __name__, url_prefix='/<string:language_code>/acp/languages')


@acp_language_blueprint.route('', methods=['GET'])
@with_language
@with_session
def languages_route():
    controller: LanguageController = sc.get(LanguageController)

    return controller.languages_page_action()

@acp_language_blueprint.route('/add', methods=['GET', 'POST'])
@with_language
@with_session
def add_language_route():
    controller: LanguageController = sc.get(LanguageController)

    match request.method:
        case 'GET':
            return controller.add_language_page_action()
        case 'POST':
            return controller.add_language_action()

@acp_language_blueprint.route('/edit', methods=['GET', 'POST'])
@with_language
@with_session
def edit_language_route():
    controller: LanguageController = sc.get(LanguageController)

    match request.method:
        case 'GET':
            return controller.edit_language_page_action()
        case 'POST':
            return controller.edit_language_action()

@acp_language_blueprint.route('/delete', methods=['POST'])
@with_language
@with_session
def delete_language_route():
    # TODO: soft delete
    controller: LanguageController = sc.get(LanguageController)

    return controller.delete_language_action()