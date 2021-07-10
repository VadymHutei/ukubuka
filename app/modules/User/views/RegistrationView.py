from flask import request

from modules.Ukubuka.view import UkubukaView


class RegistrationView(UkubukaView):

    def prepareTemplateData(self):
        super().prepareTemplateData()
        self.data['t']['language'] = request.cnx.get('language')