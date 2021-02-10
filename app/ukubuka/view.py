from flask import render_template


class View:

    _template = None
    _data = {}

    def __init__(self, template):
        self._template = template

    def addData(self, data):
        self._data.update(data)

    def render(self):
        return render_template(self._template, **self._data)