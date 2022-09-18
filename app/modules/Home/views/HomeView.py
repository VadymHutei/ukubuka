from flask import g
from modules.Base.views.ACPView import ACPView


class HomeView(ACPView):

    template: str = 'modules/Home/homepage.html'

    def _prepare_template_data(self):
        super()._prepare_template_data()

        self.template_data['title'] = g.t._('Ukubuka')
