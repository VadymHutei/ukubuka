from modules.Ukubuka.views.UkubukaView import UkubukaView
from modules.Session.service import SessionService


class HomeController:

    def __init__(self):
        self.view = UkubukaView('modules/Home/homepage.html')

    def homeAction(self):
        sessionService = SessionService()
        return self.view.render()