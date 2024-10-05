from flask import Blueprint

from blueprints.blueprint_names import PRODUCT_BLUEPRINT
from controllers.webstore.ProductController import ProductController
from modules.Session.requestDecorators import with_session
from request_decorators import with_language, with_currency
from service_container import sc

product_blueprint = Blueprint(PRODUCT_BLUEPRINT, __name__, url_prefix='/<string:language_code>/product')


@product_blueprint.route('<string:product_slug>', methods=['GET'])
@with_session
@with_language
@with_currency
def product_page_route(product_slug: str):
    controller: ProductController = sc.get(ProductController)

    return controller.product_page_action(product_slug)
