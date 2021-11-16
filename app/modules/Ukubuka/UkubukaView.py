from flask import request

from modules.Language.service import LanguageService
from vendor.ukubuka.view import View


class UkubukaView(View):

    def _prepareTemplateData(self):
        super()._prepareTemplateData()

        languageService = LanguageService.getInstance()
        self._templateData['request'] = {
            'path': request.path,
        }
        self._templateData['language'] = request.ctx.get('language')
        self._templateData['languages'] = languageService.languages
        self._templateData['sessionID'] = request.ctx.get('sessionID')
        self._templateData['user'] = request.ctx.get('user')