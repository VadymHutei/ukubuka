from flask import g

from modules.Ukubuka.views.UkubukaACPView import UkubukaACPView


class CategoryACPView(UkubukaACPView):
    
    def __init__(self):
        super().__init__('modules/Category/ACP/categories.html')

    def _prepareTemplateData(self):
        super()._prepareTemplateData()

        self.templateData['title'] = g.t._('Categories')