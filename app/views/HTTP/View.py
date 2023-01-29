from flask import render_template

from views.AbstractView import AbstractView


class View(AbstractView):

    TEMPLATE: str

    _title: str

    def __init__(self):
        self._template_data = {}
        self._data = {}

    def _prepare_data(self):
        self._prepare_page_data()
        self._prepare_template_data()
        self._data['t'] = self._template_data

    def _prepare_page_data(self):
        pass

    def _prepare_template_data(self):
        self._template_data['title'] = self._title

    def render(self):
        self._prepare_data()

        return render_template(self.TEMPLATE, **self._data)