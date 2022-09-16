from flask import g
from modules.Ukubuka.views.UkubukaACPView import UkubukaACPView


class TranslationsACPView(UkubukaACPView):

    template: str = 'modules/Language/ACP/translations.html'

    def _prepare_template_data(self):
        super()._prepare_template_data()

        self.template_data['title'] = g.t._('Translations')
