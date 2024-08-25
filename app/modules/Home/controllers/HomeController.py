from views.HTML.website.HomeView import HomeView


class HomeController:

    def home_page_action(self):
        view = HomeView()

        return view.render()
