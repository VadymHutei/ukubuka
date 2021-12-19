from flask import Blueprint, redirect, url_for, g

from modules.Home.controllers.HomeController import HomeController
from modules.Language.requestDecorators import languageRedirect
from modules.Session.requestDecorators import withSession


homeBlueprint = Blueprint('homeBlueprint', __name__)

@homeBlueprint.route('/', methods=['GET'])
@withSession
def mainRedirect():
    return redirect(url_for('homeRoute', language=g.t.defaultLanguage.code))


@homeBlueprint.route('/<string:language>/', methods=['GET'])
@languageRedirect
@withSession
def homeRoute():
    controller = HomeController()
    return controller.homeAction()