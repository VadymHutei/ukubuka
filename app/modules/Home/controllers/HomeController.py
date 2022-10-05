from modules.Home.views.HomeView import HomeView


class HomeController:

    def home_action(self):
        view = HomeView()
        return view.render()
