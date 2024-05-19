from flask import Blueprint

from blueprints.blueprint_names import PRODUCT_BLUEPRINT
from controllers.webstore.ProductController import ProductController
from modules.Session.requestDecorators import with_session
from request_decorators import with_language
from service_container import sc

product_blueprint = Blueprint(PRODUCT_BLUEPRINT, __name__, url_prefix='/<string:language>/products')


@product_blueprint.route('<string:code>', methods=['GET'])
@with_language
@with_session
def product_route(code: str):
    controller: ProductController = sc.get(ProductController)

    return controller.product_page_action(code)