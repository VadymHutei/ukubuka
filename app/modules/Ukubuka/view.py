from flask import request

from vendor.Ukubuka.view import View


class UkubukaView(View):

    def prepareTemplateData(self):
        super().prepareTemplateData()
        self.templateData['language'] = request.cnx.get('language')
        self.templateData['sessionID'] = request.cnx.get('sessionID')
        self.templateData['user'] = request.cnx.get('user')