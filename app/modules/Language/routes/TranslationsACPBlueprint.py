from flask import Blueprint, request, redirect, url_for

from modules.Language.controllers.TranslationACPController import TranslationACPController
from modules.Language.requestDecorators import languageRedirect
from modules.Session.requestDecorators import withSession


translationsACPBlueprint = Blueprint('translationsACPBlueprint', __name__, url_prefix='/<string:language>/acp/translations')
translationsACPController = TranslationACPController()

@translationsACPBlueprint.route('', methods=['GET'])
@languageRedirect
@withSession
def translationsACPRoute():
    return translationsACPController.translationsPageAction()

@translationsACPBlueprint.route('/edit', methods=['GET', 'POST'])
@languageRedirect
@withSession
def editTranslationACPRoute():
    if request.method == 'GET':
        return translationsACPController.editTranslationsPageAction()
    elif request.method == 'POST':
        return translationsACPController.editTranslationsAction()

@translationsACPBlueprint.route('/delete', methods=['GET'])
@languageRedirect
@withSession
def deleteTranslationACPRoute():
    return translationsACPController.deleteTextAction()