from modules.Ukubuka.view import UkubukaView


class DashboardController:

    def dashboardAction(self):
        view = UkubukaView('modules/ACP/Dashboard/dashboard.html')
        return view.render()