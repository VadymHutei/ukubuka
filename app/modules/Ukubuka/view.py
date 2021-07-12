from flask import request

from vendor.Ukubuka.view import View


class UkubukaView(View):

    def prepareTemplateData(self):
        super().prepareTemplateData()
        self.templateData['language'] = request.ctx.get('language')
        self.templateData['sessionID'] = request.ctx.get('sessionID')
        self.templateData['user'] = request.ctx.get('user')