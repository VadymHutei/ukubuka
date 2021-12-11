from modules.Ukubuka.views.UkubukaACPView import UkubukaACPView
from modules.Language.services.LanguageService import LanguageService


class UsersACPView(UkubukaACPView):

    def __init__(self):
        super().__init__('modules/User/ACP/users.html')

    def _prepareTemplateData(self):
        super()._prepareTemplateData()

        languageService = LanguageService.getInstance()
        self.templateData['title'] = languageService.translate('Translations')