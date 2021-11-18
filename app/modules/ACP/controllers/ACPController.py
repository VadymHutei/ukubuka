from modules.ACP.views.ACPDashboardView import ACPDashboardView


class ACPController:

    def dashboardAction(self):
        view = ACPDashboardView()
        return view.render()