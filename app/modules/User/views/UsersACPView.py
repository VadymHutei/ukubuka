from flask import g

from modules.Ukubuka.views.UkubukaACPView import UkubukaACPView


class UsersACPView(UkubukaACPView):

    def __init__(self):
        super().__init__('modules/User/ACP/users.html')

    def _prepareTemplateData(self):
        super()._prepareTemplateData()

        self.templateData['title'] = g.t._('Users')