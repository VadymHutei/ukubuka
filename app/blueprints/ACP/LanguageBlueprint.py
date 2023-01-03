from flask import Blueprint
from modules.Language.requestDecorators import language_redirect
from modules.Session.requestDecorators import with_session

BLUEPRINT_NAME = 'ACP_language_blueprint'
language_blueprint = Blueprint(BLUEPRINT_NAME, __name__, url_prefix='/<string:language>/acp/languages')


@language_blueprint.route('', methods=['GET'])
@language_redirect
@with_session
def language_route():
    return 'languages'
