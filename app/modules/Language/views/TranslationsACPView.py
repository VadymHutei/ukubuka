from flask import g

from modules.Ukubuka.views.UkubukaACPView import UkubukaACPView


class TranslationsACPView(UkubukaACPView):

    def __init__(self):
        super().__init__('modules/Language/ACP/translations.html')

    def _prepareTemplateData(self):
        super()._prepareTemplateData()

        self.templateData['title'] = g.t._('Translations')