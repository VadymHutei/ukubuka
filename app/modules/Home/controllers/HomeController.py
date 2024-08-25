from views.HTML.website.HomeView import HomeView
from flask import current_app as app


class HomeController:

    def home_page_action(self):
        view = HomeView()

        view.set_data(
            urls=app.url_map.iter_rules()
        )

        return view.render()
