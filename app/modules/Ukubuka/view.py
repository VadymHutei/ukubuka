from flask import request

from modules.Language.service import LanguageService
from vendor.Ukubuka.view import View


class UkubukaView(View):

    def prepareTemplateData(self):
        super().prepareTemplateData()

        languageService = LanguageService.getInstance()
        self.templateData['request'] = {
            'path': request.path,
        }
        self.templateData['language'] = request.ctx.get('language')
        self.templateData['languages'] = languageService.getAvailableLanguages()
        self.templateData['sessionID'] = request.ctx.get('sessionID')
        self.templateData['user'] = request.ctx.get('user')