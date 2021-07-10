from flask import request

from modules.Ukubuka.view import UkubukaView


class HomeView(UkubukaView):

    def prepareTemplateData(self):
        super().prepareTemplateData()