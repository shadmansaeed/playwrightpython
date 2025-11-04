from .dashboard import DashboardPage


class LoginPage:
    def __init__(self, page):  # constractor
        self.page = page

    def navigate(self):
        self.page.goto("https://rahulshettyacademy.com/client")

    def login(self,userEmail,userPassword):
        self.page.get_by_placeholder("email@example.com").fill(userEmail)
        self.page.get_by_placeholder("enter your passsword").fill(userPassword)

        self.page.get_by_role("button", name="Login").click()
        dashboardPage = DashboardPage(self.page) #eita sudhu sudhu likhlei hobena. jodi oi page er dahboard e land kore tahole eivabe object likhle kaj hobe
        return dashboardPage
