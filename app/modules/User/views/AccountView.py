from modules.Base.views.LayoutView import LayoutView


class AccountView(LayoutView):

    page_title: str = 'Account'
    template: str = 'modules/User/account.html'
