from flask import Blueprint

from modules.Category.controllers.CategoryACPController import CategoryACPController
from modules.Session.requestDecorators import with_session
from request_decorators import with_language

categoryACPBlueprint = Blueprint('categoryACPBlueprint', __name__, url_prefix='/<string:language>/acp/categories')
categoryACPController = CategoryACPController()


@categoryACPBlueprint.route('', methods=['GET'])
@with_language
@with_session
def categoriesACPRoute():
    return categoryACPController.categoriesPageAction()
