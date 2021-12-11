from modules.Language.services.LanguageService import LanguageService
from modules.Ukubuka.views.UkubukaACPView import UkubukaACPView


class TranslationsACPView(UkubukaACPView):

    def __init__(self):
        super().__init__('modules/Language/ACP/translations.html')

    def _prepareTemplateData(self):
        super()._prepareTemplateData()

        languageService = LanguageService.getInstance()
        self.templateData['title'] = languageService.translate('Translations')