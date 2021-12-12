from modules.Home.views.HomeView import HomeView


class HomeController:

    def homeAction(self):
        view = HomeView()
        return view.render()