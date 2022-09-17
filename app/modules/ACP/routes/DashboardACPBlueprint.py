from flask import Blueprint
from modules.ACP.controllers.DashboardACPController import DashboardACPController
from modules.Language.requestDecorators import language_redirect
from modules.Session.requestDecorators import withSession

dashboardACPBlueprint = Blueprint('dashboardACPBlueprint', __name__,)
controller = DashboardACPController()


@dashboardACPBlueprint.route('/<string:language>/acp', methods=['GET'])
@language_redirect
@withSession
def dashboardACPRoute():
    return controller.dashboardAction()
