from flask import Blueprint

from controllers.HTTP.ACP.LanguageController import LanguageController
from modules.Language.requestDecorators import language_redirect
from modules.Session.requestDecorators import with_session
from service_container import sc

BLUEPRINT_NAME = 'ACP_language_blueprint'
acp_language_blueprint = Blueprint(BLUEPRINT_NAME, __name__, url_prefix='/<string:language>/acp/languages')


@acp_language_blueprint.route('', methods=['GET'])
@language_redirect
@with_session
def language_route():
    controller: LanguageController = sc.get(LanguageController)
    return controller.languages_page_action()