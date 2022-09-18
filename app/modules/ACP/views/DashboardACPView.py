from flask import g
from modules.Base.views.ACPView import ACPView


class DashboardACPView(ACPView):

    template: str = 'modules/ACP/dashboard.html'

    def _prepare_template_data(self):
        super()._prepare_template_data()

        self.template_data['title'] = g.t._('Dashboard')
