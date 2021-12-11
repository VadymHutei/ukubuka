from modules.ACP.views.DashboardACPView import DashboardACPView


class ACPController:

    def dashboardAction(self):
        view = DashboardACPView()
        return view.render()