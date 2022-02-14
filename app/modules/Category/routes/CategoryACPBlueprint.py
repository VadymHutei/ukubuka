from flask import Blueprint

from modules.Category.controllers.CategoryACPController import CategoryACPController
from modules.Language.requestDecorators import languageRedirect
from modules.Session.requestDecorators import withSession


categoryACPBlueprint = Blueprint('categoryACPBlueprint', __name__, url_prefix='/<string:language>/acp/categories')
categoryACPController = CategoryACPController()


@categoryACPBlueprint.route('', methods=['GET'])
@languageRedirect
@withSession
def categoriesACPRoute():
    return categoryACPController.categoriesPageAction()