from flask import g
from modules.Base.views.ACPView import ACPView


class HomeView(ACPView):

    template: str = 'modules/Home/homepage.html'
    page_title: str = 'Ukubuka'
