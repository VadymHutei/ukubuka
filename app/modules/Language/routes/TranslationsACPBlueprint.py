from flask import Blueprint, request
from modules.Language.controllers.TranslationACPController import TranslationACPController
from modules.Language.requestDecorators import language_redirect
from modules.Session.requestDecorators import withSession

translationsACPBlueprint = Blueprint('translationsACPBlueprint', __name__,
                                     url_prefix='/<string:language>/acp/translations')
translationsACPController = TranslationACPController()


@translationsACPBlueprint.route('', methods=['GET'])
@language_redirect
@withSession
def translationsACPRoute():
    return translationsACPController.translationsPageAction()


@translationsACPBlueprint.route('/edit', methods=['GET', 'POST'])
@language_redirect
@withSession
def editTranslationACPRoute():
    if request.method == 'GET':
        return translationsACPController.editTranslationsPageAction()
    elif request.method == 'POST':
        return translationsACPController.editTranslationsAction()


@translationsACPBlueprint.route('/delete', methods=['GET'])
@language_redirect
@withSession
def deleteTranslationACPRoute():
    return translationsACPController.deleteTextAction()
