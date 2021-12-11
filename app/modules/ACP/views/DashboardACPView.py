from modules.Language.services.LanguageService import LanguageService
from modules.Ukubuka.views.UkubukaACPView import UkubukaACPView


class DashboardACPView(UkubukaACPView):

    def __init__(self):
        super().__init__('modules/ACP/dashboard.html')

    def _prepareTemplateData(self):
        super()._prepareTemplateData()

        languageService = LanguageService.getInstance()
        self.templateData['title'] = languageService.translate('Dashboard')