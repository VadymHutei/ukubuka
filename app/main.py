from flask import Flask

from container import Container


app = Flask(__name__)
container = Container()

@app.route('/')
def homePage():
    controller = container.get('HomePageController')
    return controller.homePageAction()