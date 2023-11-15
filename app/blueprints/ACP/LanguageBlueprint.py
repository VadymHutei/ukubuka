from flask import Blueprint, request

from blueprints.blueprint_names import ACP_LANGUAGE_BLUEPRINT
from controllers.ACP.LanguageController import LanguageController
from modules.Language.requestDecorators import language_redirect
from modules.Session.requestDecorators import with_session
from service_container import sc


acp_language_blueprint = Blueprint(ACP_LANGUAGE_BLUEPRINT, __name__, url_prefix='/<string:language>/acp/languages')


@acp_language_blueprint.route('', methods=['GET'])
@language_redirect
@with_session
def languages_route() -> str:
    controller: LanguageController = sc.get(LanguageController)

    return controller.languages_page_action()

@acp_language_blueprint.route('/edit', methods=['GET', 'POST'])
@language_redirect
@with_session
def edit_language_route() -> str:
    if request.method == 'GET':
        controller: LanguageController = sc.get(LanguageController)

        language_code = request.args.get('code')

        return controller.edit_language_page_action(language_code)
    else:
        return 'DONE'

@acp_language_blueprint.route('/delete', methods=['GET'])
@language_redirect
@with_session
def delete_language_route(language_code: str):
    controller: LanguageController = sc.get(LanguageController)

    language_code = request.args.get('code')

    return controller.delete_language_page_action(language_code)