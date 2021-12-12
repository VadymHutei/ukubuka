from flask import Blueprint, request

from modules.Language.controllers.TranslationACPController import TranslationACPController
from modules.Language.requestDecorators import languageRedirect
from modules.Session.requestDecorators import withSession


translationsACPBlueprint = Blueprint('translationsACPBlueprint', __name__, url_prefix='/<string:language>/acp/translations')
translationsACPController = TranslationACPController()

@translationsACPBlueprint.route('', methods=['GET'])
@languageRedirect
@withSession
def translationsACPRoute():
    return translationsACPController.translationsAction()

@translationsACPBlueprint.route('/edit', methods=['GET', 'POST'])
@languageRedirect
@withSession
def editTranslationACPRoute():
    if request.method == 'GET':
        return translationsACPController.editPageAction()
    elif request.method == 'POST':
        return translationsACPController.editAction()
    return translationsACPController.translationsAction()

@translationsACPBlueprint.route('/delete', methods=['GET', 'POST'])
@languageRedirect
@withSession
def deleteTranslationACPRoute():
    if request.method == 'GET':
        return translationsACPController.deletePageAction()
    elif request.method == 'POST':
        return translationsACPController.deleteAction()