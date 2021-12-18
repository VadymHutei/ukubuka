from modules.Ukubuka.views.UkubukaACPView import UkubukaACPView
from modules.Language.services.LanguageService import LanguageService


class EditUserACPView(UkubukaACPView):

    def __init__(self):
        super().__init__('modules/User/ACP/editUser.html')

        self.languageService = LanguageService.getInstance()

    def _prepareTemplateData(self):
        super()._prepareTemplateData()

        self.templateData['title'] = self.languageService.translate('Translations')