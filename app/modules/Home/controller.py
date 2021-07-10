from flask import request

from modules.Home.view import HomeView
from modules.Session.service import SessionService


class HomeController:

    def __init__(self):
        self.view = HomeView('modules/Home/page.html')

    def homeAction(self):
        sessionService = SessionService()
        self.view.addData({
            'sessionID': request.cnx['sessionID'],
        })
        return self.view.render()