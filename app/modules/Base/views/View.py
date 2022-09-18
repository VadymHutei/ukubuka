from flask import g, render_template


class View:

    template: str
    page_title: str

    def __init__(self):
        self.data = {}
        self.template_data = {}

    def _prepage_data(self):
        self._prepare_template_data()
        self._prepare_page_data()
        self.data['t'] = self.template_data

    def _prepare_template_data(self):
        self.template_data['title'] = g.t._(self.page_title)
        self.template_data['language'] = g.current_language

    def _prepare_page_data(self):
        pass

    def render(self):
        self._prepage_data()
        return render_template(self.template, **self.data)
