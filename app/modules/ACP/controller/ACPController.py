from flask import abort

from modules.ACP.view.ACPView import ACPView
from modules.ACP.view.CategoriesView import CategoriesView


class ACPController:

    def __init__(self, service):
        self._service = service

    def ACPAction(self, language=None):
        view = ACPView(language=language)
        return view.render()

    def categoriesAction(self):
        categories = self._service.getCategories()
        view =  ()
        view.addData({'categories': categories})
        return view.render()