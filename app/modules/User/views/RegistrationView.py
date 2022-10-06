from modules.Base.views.LayoutView import LayoutView


class RegistrationView(LayoutView):

    page_title: str = 'Registration'
    template: str = 'modules/User/registration.html'
