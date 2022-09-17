from flask import Blueprint, g, redirect, url_for
from modules.Home.controllers.HomeController import HomeController
from modules.Language.requestDecorators import language_redirect
from modules.Session.requestDecorators import withSession

homeBlueprint = Blueprint('homeBlueprint', __name__)


@homeBlueprint.route('/', methods=['GET'])
@withSession
def mainRedirect():
    return redirect(url_for('homeBlueprint.homeRoute', language=g.t.default_language.code))


@homeBlueprint.route('/<string:language>/', methods=['GET'])
@language_redirect
@withSession
def homeRoute():
    controller = HomeController()
    return controller.homeAction()
