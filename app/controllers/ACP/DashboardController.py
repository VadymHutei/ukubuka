from controllers.IController import IController
from views.HTML.ACP.Dashboard.DashboardView import DashboardView


class DashboardController(IController):

    def dashboard_page_action(self):
        view: DashboardView = DashboardView()

        return view.render()