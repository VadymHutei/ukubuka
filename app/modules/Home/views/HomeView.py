from modules.Base.views.LayoutView import LayoutView


class HomeView(LayoutView):

    page_title: str = 'Ukubuka'
    template: str = 'modules/Home/homepage.html'
