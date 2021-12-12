from modules.Ukubuka.views.UkubukaACPView import UkubukaACPView
from modules.Language.services.LanguageService import LanguageService


class HomeView(UkubukaACPView):

    def __init__(self):
        super().__init__('modules/Home/homepage.html')
        
        self.languageService = LanguageService.getInstance()

    def _prepareTemplateData(self):
        super()._prepareTemplateData()

        self.templateData['title'] = self.languageService.translate('Ukubuka')