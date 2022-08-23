from flask import request, g

from modules.Base.view import View


class UkubukaView(View):

    def _prepareTemplateData(self):
        super()._prepareTemplateData()

        self.templateData.update({
            'request': {
                'path': request.path,
            },
            'language': request.ctx.get('language'),
            'languages': g.t.languages,
            'sessionID': request.ctx.get('sessionID'),
            'user': request.ctx.get('user'),
        })