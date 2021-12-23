from modules.ACP.views.DashboardACPView import DashboardACPView


class DashboardACPController:

    def dashboardAction(self):
        view = DashboardACPView()
        
        return view.render()