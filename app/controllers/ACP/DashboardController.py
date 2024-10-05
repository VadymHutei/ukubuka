from controllers.Controller import Controller
from views.HTML.ACP.Dashboard.DashboardView import DashboardView


class DashboardController(Controller):

    def dashboard_page_action(self):
        view: DashboardView = DashboardView()

        return view.render()