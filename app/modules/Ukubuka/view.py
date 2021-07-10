from flask import request

from vendor.Ukubuka.view import View


class UkubukaView(View):

    def prepareTemplateData(self):
        super().prepareTemplateData()
        self.data['t']['language'] = request.cnx.get('language')
        self.data['t']['sessionID'] = request.cnx.get('sessionID')
        self.data['t']['user'] = request.cnx.get('user')