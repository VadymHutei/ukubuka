from modules.Language.service import LanguageService
from modules.Ukubuka.UkubukaACPView import UkubukaACPView


class ACPTranslationEditView(UkubukaACPView):

    def __init__(self):
        super().__init__('modules/Language/ACP/TranslationEdit.html')

    def prepareTemplateData(self):
        super().prepareTemplateData()

        languageService = LanguageService.getInstance()
        self.templateData['title'] = languageService.translate('Edit translation')
