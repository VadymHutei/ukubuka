from flask import g, request
from modules.Base.view import View


class UkubukaView(View):

    def _prepareTemplateData(self):
        super()._prepareTemplateData()

        self.templateData.update({
            'request': {
                'path': request.path,
            },
            'language': g.current_language,
            'languages': g.t.languages,
            'sessionID': request.ctx.get('sessionID'),
            'user': request.ctx.get('user'),
        })
