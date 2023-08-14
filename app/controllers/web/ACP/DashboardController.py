from service_container import sc
from views.HTML.ACP.Dashboard.DashboardView import DashboardView
from views.ViewFactory import ViewFactory


class DashboardController:

    def dashboard_page_action(self):
        view_factory: ViewFactory = sc.get(ViewFactory)
        view: DashboardView = view_factory.get(DashboardView)

        return view.render()