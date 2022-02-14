from modules.Category.services.CategoryService import CategoryService
from modules.Category.views.CategoryACPView import CategoryACPView


class CategoryACPController:

    def __init__(self):
        self._categoryService = CategoryService()

    def categoriesPageAction(self):
        view = CategoryACPView()

        categories = self._categoryService.getCategories()

        view.data = {
            'categories': categories
        }

        return view.render()