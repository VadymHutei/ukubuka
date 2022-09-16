from flask import g, url_for
from modules.Ukubuka.views.UkubukaACPView import UkubukaACPView


class EditUserACPView(UkubukaACPView):

    template: str = 'modules/User/ACP/editUser.html'

    def _prepage_data(self):
        super()._prepage_data()

        self.data['form_url'] = url_for(
            endpoint='ACP_user_Blueprint.ACP_edit_user_route',
            language=g.current_language.code,
            id=self.data['user'].ID,
        )

    def _prepare_template_data(self):
        super()._prepare_template_data()

        self.template_data['title'] = g.t._('Edit user')
