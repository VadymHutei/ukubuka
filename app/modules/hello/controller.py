class HelloController:
    def __init__(self, view):
        self.view = view

    def helloAction(self):
        return self.view.render()