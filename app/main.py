from flask import Flask

from container import Container


app = Flask(__name__)
container = Container()

@app.route('/')
def hello_world():
    controller = container.get('HelloController')
    return controller.helloAction()