from flask import render_template


class HomePageView:

    def render(self):
        return render_template('home_page/page.html')