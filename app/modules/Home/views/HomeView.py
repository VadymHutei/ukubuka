from flask import g
from modules.Ukubuka.views.UkubukaACPView import UkubukaACPView


class HomeView(UkubukaACPView):

    template: str = 'modules/Home/homepage.html'

    def _prepare_template_data(self):
        super()._prepare_template_data()

        self.template_data['title'] = g.t._('Ukubuka')
