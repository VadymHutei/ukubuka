from flask import g
from modules.Base.views.ACPView import ACPView


class CategoryACPView(ACPView):

    template: str = 'modules/Category/ACP/categories.html'

    def _prepare_template_data(self):
        super()._prepare_template_data()

        self.template_data['title'] = g.t._('Categories')
