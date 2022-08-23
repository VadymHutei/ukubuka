from flask import render_template


class View:

    def __init__(self, template=None):
        self.template = template
        self.data = {}
        self.templateData = {}

    def _prepageData(self):
        self._prepareTemplateData()
        self._preparePageData()
        self.data['t'] = self.templateData

    def _prepareTemplateData(self):
        pass

    def _preparePageData(self):
        pass

    def render(self):
        self._prepageData()
        return render_template(self.template, **self.data)