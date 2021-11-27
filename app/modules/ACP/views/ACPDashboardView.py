from modules.Language.service import LanguageService
from modules.Ukubuka.views.UkubukaACPView import UkubukaACPView


class ACPDashboardView(UkubukaACPView):

    def __init__(self):
        super().__init__('modules/ACP/dashboard.html')

    def _prepareTemplateData(self):
        super()._prepareTemplateData()

        languageService = LanguageService.getInstance()
        self.templateData['title'] = languageService.translate('Dashboard')