from flask import Blueprint

from modules.ACP.controllers.DashboardACPController import DashboardACPController
from modules.Language.requestDecorators import languageRedirect
from modules.Session.requestDecorators import withSession


dashboardACPBlueprint = Blueprint('dashboardACPBlueprint', __name__,)
controller = DashboardACPController()

@dashboardACPBlueprint.route('/<string:language>/acp', methods=['GET'])
@languageRedirect
@withSession
def dashboardACPRoute():
    return controller.dashboardAction()