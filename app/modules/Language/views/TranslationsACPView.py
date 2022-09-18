from flask import g
from modules.Base.views.ACPView import ACPView


class TranslationsACPView(ACPView):

    template: str = 'modules/Language/ACP/translations.html'

    def _prepare_template_data(self):
        super()._prepare_template_data()

        self.template_data['title'] = g.t._('Translations')
