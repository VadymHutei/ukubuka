from flask import request
from modules.Base.views.View import View
from modules.Language.services.LanguageService import LanguageService


class LayoutView(View):

    def __init__(self):
        super().__init__()

        self.layout_data = {}

    def _prepare_layout_data(self):
        language_service = LanguageService()
        self.layout_data['languages'] = language_service.get_languages(only_active=True)
        self.layout_data['requested_path'] = request.path
        self.layout_data['request_endpoint'] = request.endpoint
        # self.layout_data['request'] = request

    def _prepare_data(self):
        super()._prepare_data()

        self._prepare_layout_data()
        self.data['l'] = self.layout_data
