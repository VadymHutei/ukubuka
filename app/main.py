from flask import Flask

from modules.hello.controller import HelloController


app = Flask(__name__)

@app.route('/')
def hello_world():
    controller = HelloController()
    return controller.helloAction()