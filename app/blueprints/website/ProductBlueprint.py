from flask import Blueprint

from blueprints.blueprint_names import PRODUCT_BLUEPRINT
from modules.Language.requestDecorators import language_redirect
from modules.Session.requestDecorators import with_session
from service_container import sc
from controllers.webstore.ProductController import ProductController


product_blueprint = Blueprint(PRODUCT_BLUEPRINT, __name__, url_prefix='/<string:language>/products')


@product_blueprint.route('<string:code>', methods=['GET'])
@language_redirect
@with_session
def product_route(code: str):
    controller: ProductController = sc.get(ProductController)

    return controller.product_page_action(code)