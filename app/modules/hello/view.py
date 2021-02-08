from flask import render_template


class HelloView:

    def render(self):
        return render_template('hello/page.html')