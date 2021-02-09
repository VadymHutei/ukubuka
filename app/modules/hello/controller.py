class HelloController:
    def __init__(self, view, foo):
        self.view = view
        print(foo)

    def helloAction(self):
        return self.view.render()