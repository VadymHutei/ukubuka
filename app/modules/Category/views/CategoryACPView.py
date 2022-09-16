from flask import g
from modules.Ukubuka.views.UkubukaACPView import UkubukaACPView


class CategoryACPView(UkubukaACPView):

    template: str = 'modules/Category/ACP/categories.html'

    def _prepare_template_data(self):
        super()._prepare_template_data()

        self.template_data['title'] = g.t._('Categories')
