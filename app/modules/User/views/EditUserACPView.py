from flask import g
from modules.Base.views.ACPView import ACPView


class EditUserACPView(ACPView):

    template: str = 'modules/User/ACP/editUser.html'
    page_title: str = 'Edit user'
