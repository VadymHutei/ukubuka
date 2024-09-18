from flask import Blueprint

from blueprints.blueprint_names import CATALOG_BLUEPRINT
from controllers.webstore.CatalogController import CatalogController
from modules.Session.requestDecorators import with_session
from request_decorators import with_language
from service_container import sc

catalog_blueprint = Blueprint(CATALOG_BLUEPRINT, __name__, url_prefix='/<string:language_code>/catalog')


@catalog_blueprint.route('<string:category_slug>', methods=['GET'])
@with_language
@with_session
def category_page_route(category_slug: str):
    controller: CatalogController = sc.get(CatalogController)

    return controller.category_page_action(category_slug)
