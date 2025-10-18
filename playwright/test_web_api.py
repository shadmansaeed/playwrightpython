from playwright.sync_api import Playwright


def test_e2e_web_api(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    # create order --> orderID

    # login
    page.goto("https://rahulshettyacademy.com/client")
    page.get_by_placeholder("email@example.com").fill("rahulshetty@gmail.com")
    page.get_by_placeholder("enter your password").fill("Iamking@000")
    page.get_by_role("button", name="Login").click()

    # orders history page --> order is present

