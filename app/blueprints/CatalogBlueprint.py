from flask import Blueprint

from blueprints.blueprint_names import CATALOG_BLUEPRINT
from modules.Language.requestDecorators import language_redirect
from modules.Session.requestDecorators import with_session


catalog_blueprint = Blueprint(CATALOG_BLUEPRINT, __name__, url_prefix='/<string:language>/catalogs')


@catalog_blueprint.route('', methods=['GET'])
@language_redirect
@with_session
def catalogs_route():
    return 'catalogs'

@catalog_blueprint.route('<string:code>', methods=['GET'])
@language_redirect
@with_session
def catalog_route(code: str):
    return 'catalog'