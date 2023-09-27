from flask import Blueprint

from blueprints.blueprint_names import CATALOG_BLUEPRINT
from controllers.webstore.CatalogController import CatalogController
from modules.Language.requestDecorators import language_redirect
from modules.Session.requestDecorators import with_session
from service_container import sc


catalog_blueprint = Blueprint(CATALOG_BLUEPRINT, __name__, url_prefix='/<string:language>/catalogs')


@catalog_blueprint.route('', methods=['GET'])
@language_redirect
@with_session
def catalogs_page_route():
    controller: CatalogController = sc.get(CatalogController)

    return controller.catalogs_page_action()

@catalog_blueprint.route('<string:catalog_code>', methods=['GET'])
@language_redirect
@with_session
def catalog_page_route(catalog_code: str):
    controller: CatalogController = sc.get(CatalogController)

    return controller.catalog_page_action(catalog_code)