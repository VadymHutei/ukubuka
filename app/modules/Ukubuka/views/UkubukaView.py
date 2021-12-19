from flask import request, g

from vendor.ukubuka.view import View


class UkubukaView(View):

    def _prepareTemplateData(self):
        super()._prepareTemplateData()

        self._templateData['request'] = {
            'path': request.path,
        }
        self._templateData['language'] = request.ctx.get('language')
        self._templateData['languages'] = g.t.languages
        self._templateData['sessionID'] = request.ctx.get('sessionID')
        self._templateData['user'] = request.ctx.get('user')