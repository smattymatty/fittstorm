from BaseApp.views import BasePage


class DashboardPage(BasePage):
    template_name = 'dashboard_app/base.html'
    page_title = "Dashboard"
    page_description = "This is the dashboard."
