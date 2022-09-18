from flask import g
from modules.Base.views.ACPView import ACPView


class UsersACPView(ACPView):

    template: str = 'modules/User/ACP/users.html'

    def _prepare_template_data(self):
        super()._prepare_template_data()

        self.template_data['title'] = g.t._('Users')
