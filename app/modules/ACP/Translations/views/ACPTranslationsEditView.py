from modules.Language.service import LanguageService
from modules.Ukubuka.view import UkubukaView


class ACPTranslationsEditView(UkubukaView):

    def prepareTemplateData(self):
        super().prepareTemplateData()

        languageService = LanguageService.getInstance()
        self.templateData['title'] = languageService.translate('Edit translations')