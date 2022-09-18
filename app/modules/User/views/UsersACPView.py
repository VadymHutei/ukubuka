from modules.Base.views.ACPView import ACPView


class UsersACPView(ACPView):

    template: str = 'modules/User/ACP/users.html'
    page_title: str = 'Users'
