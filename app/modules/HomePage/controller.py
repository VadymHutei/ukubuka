class HomePageController:

    def __init__(self, view):
        self.view = view

    def homePageAction(self):
        return self.view.render()