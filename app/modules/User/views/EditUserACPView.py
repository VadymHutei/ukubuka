from flask import g

from modules.Ukubuka.views.UkubukaACPView import UkubukaACPView


class EditUserACPView(UkubukaACPView):

    def __init__(self):
        super().__init__('modules/User/ACP/editUser.html')

    def _prepareTemplateData(self):
        super()._prepareTemplateData()

        self.templateData['title'] = g.t._('Edit user')