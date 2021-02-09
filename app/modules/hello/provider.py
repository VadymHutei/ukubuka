from modules.hello.controller import HelloController
from modules.hello.view import HelloView


class HelloProvider:

    @staticmethod
    def getResources():
        return {
            HelloController: (HelloView, 'bar'),
            HelloView: ()
        }