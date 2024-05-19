from flask import Blueprint

from blueprints.blueprint_names import ACP_DASHBOARD_BLUEPRINT
from controllers.ACP.DashboardController import DashboardController
from modules.Session.requestDecorators import with_session
from request_decorators import with_language
from service_container import sc

acp_dashboard_blueprint = Blueprint(ACP_DASHBOARD_BLUEPRINT, __name__, url_prefix='/<string:language>/acp')


@acp_dashboard_blueprint.route('', methods=['GET'])
@with_language
@with_session
def dashboard_page_route():
    controller: DashboardController = sc.get(DashboardController)

    return controller.dashboard_page_action()