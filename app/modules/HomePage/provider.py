from modules.HomePage.controller import HomePageController
from modules.HomePage.view import HomePageView


class HomePageProvider:

    @staticmethod
    def getResources():
        return {
            HomePageController: (HomePageView,),
            HomePageView: ()
        }