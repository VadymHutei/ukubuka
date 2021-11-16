from modules.Ukubuka.UkubukaView import UkubukaView


class ACPCategoriesController:

    def categoriesAction(self):
        view = UkubukaView('modules/ACP/Categories/categories.html')
        return view.render