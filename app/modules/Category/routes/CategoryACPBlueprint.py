from flask import Blueprint
from modules.Category.controllers.CategoryACPController import CategoryACPController
from modules.Language.requestDecorators import language_redirect
from modules.Session.requestDecorators import with_session

categoryACPBlueprint = Blueprint('categoryACPBlueprint', __name__, url_prefix='/<string:language>/acp/categories')
categoryACPController = CategoryACPController()


@categoryACPBlueprint.route('', methods=['GET'])
@language_redirect
@with_session
def categoriesACPRoute():
    return categoryACPController.categoriesPageAction()
