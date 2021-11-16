from modules.Ukubuka.UkubukaView import UkubukaView


class DashboardController:

    def dashboardAction(self):
        view = UkubukaView('modules/ACP/Dashboard/dashboard.html')
        return view.render()