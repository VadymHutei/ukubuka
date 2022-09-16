from flask import g, request
from modules.Base.view import View


class UkubukaView(View):

    def _prepare_template_data(self):
        super()._prepare_template_data()

        self.template_data.update({
            'request': {
                'path': request.path,
            },
            'language': g.current_language,
            'languages': g.t.languages,
            'sessionID': request.ctx.get('sessionID'),
            'user': request.ctx.get('user'),
        })
