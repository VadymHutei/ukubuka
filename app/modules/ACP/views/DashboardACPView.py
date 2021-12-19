from flask import g

from modules.Ukubuka.views.UkubukaACPView import UkubukaACPView


class DashboardACPView(UkubukaACPView):

    def __init__(self):
        super().__init__('modules/ACP/dashboard.html')

    def _prepareTemplateData(self):
        super()._prepareTemplateData()

        self.templateData['title'] = g.t._('Dashboard')