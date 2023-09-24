from views.HTML.ACP.Dashboard.DashboardView import DashboardView


class DashboardController:

    def dashboard_page_action(self):
        view: DashboardView = DashboardView()

        return view.render()