from modules.Base.views.LayoutView import LayoutView


class LoginView(LayoutView):

    page_title: str = 'Login'
    template: str = 'modules/User/login.html'
