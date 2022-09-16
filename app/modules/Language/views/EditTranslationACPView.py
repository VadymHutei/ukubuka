from flask import g
from modules.Ukubuka.views.UkubukaACPView import UkubukaACPView


class EditTranslationACPView(UkubukaACPView):

    template: str = 'modules/Language/ACP/editTranslation.html'

    def _prepare_template_data(self):
        super()._prepare_template_data()

        self.template_data['title'] = g.t._('Edit translation')
