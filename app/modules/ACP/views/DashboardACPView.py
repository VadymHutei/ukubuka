from flask import g
from modules.Ukubuka.views.UkubukaACPView import UkubukaACPView


class DashboardACPView(UkubukaACPView):

    template: str = 'modules/ACP/dashboard.html'

    def _prepare_template_data(self):
        super()._prepare_template_data()

        self.template_data['title'] = g.t._('Dashboard')
