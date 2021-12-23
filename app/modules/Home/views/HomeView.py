from flask import g

from modules.Ukubuka.views.UkubukaACPView import UkubukaACPView


class HomeView(UkubukaACPView):

    def __init__(self):
        super().__init__('modules/Home/homepage.html')

    def _prepareTemplateData(self):
        super()._prepareTemplateData()

        self.templateData['title'] = g.t._('Ukubuka')