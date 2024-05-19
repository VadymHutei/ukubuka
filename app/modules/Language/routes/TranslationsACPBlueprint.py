from flask import Blueprint, request

from modules.Language.controllers.TranslationACPController import TranslationACPController
from modules.Session.requestDecorators import with_session
from request_decorators import with_language

translationsACPBlueprint = Blueprint(
    'translationsACPBlueprint',
    __name__,
    url_prefix='/<string:language>/acp/translations',
)
translationsACPController = TranslationACPController()


@translationsACPBlueprint.route('', methods=['GET'])
@with_language
@with_session
def translationsACPRoute():
    return translationsACPController.translationsPageAction()


@translationsACPBlueprint.route('/edit', methods=['GET', 'POST'])
@with_language
@with_session
def editTranslationACPRoute():
    if request.method == 'GET':
        return translationsACPController.editTranslationsPageAction()
    elif request.method == 'POST':
        return translationsACPController.editTranslationsAction()


@translationsACPBlueprint.route('/delete', methods=['GET'])
@with_language
@with_session
def deleteTranslationACPRoute():
    return translationsACPController.deleteTextAction()
