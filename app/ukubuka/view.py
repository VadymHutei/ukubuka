from flask import render_template


class View:

    _data = {}

    def __init__(self, template=None, language=None):
        if template is not None:
            self._template = template

        if language is not None:
            self._language = language

    def addData(self, data):
        self._data.update(data)

    def render(self):
        self._prepageData()
        return render_template(self._template, **self._data)

    def _prepageData(self):
        self._prepareLayoutData()
        self._preparePageData()

    def _prepareLayoutData(self):
        if self._language is not None:
            self._data['language'] = self._language

    def _preparePageData(self):
        pass