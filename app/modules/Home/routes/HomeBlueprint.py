from flask import Blueprint, g, redirect, url_for
from modules.Home.controllers.HomeController import HomeController
from modules.Language.requestDecorators import language_redirect
from modules.Session.requestDecorators import with_session

homeBlueprint = Blueprint('homeBlueprint', __name__)


@homeBlueprint.route('/', methods=['GET'])
@with_session
def mainRedirect():
    return redirect(url_for('homeBlueprint.homeRoute', language=g.t.default_language.code))


@homeBlueprint.route('/<string:language>/', methods=['GET'])
@language_redirect
@with_session
def homeRoute():
    controller = HomeController()
    return controller.homeAction()
