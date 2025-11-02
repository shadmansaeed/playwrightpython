from playwright.sync_api import Playwright, expect

from utils.apiBase1 import APIUtils


def test_e2e_web_api(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    # create order --> orderID

    api_Utils = APIUtils()
    orderId = api_Utils.createOrder(playwright)

    # login
    page.goto("https://rahulshettyacademy.com/client")
    page.get_by_placeholder("email@example.com").fill("rahulshetty@gmail.com")
    page.get_by_placeholder("enter your passsword").fill("Iamking@000")
    page.get_by_role("button", name="Login").click()

    # Click on Orders
    page.get_by_role("button", name="ORDERS").click()

    # orders history page --> order is present
    row= page.locator("tr").filter(has_text=orderId)  # orderid dile exact orderid khuje pabe
    row.get_by_role("button", name="View").click()  # ekhane row. use korar jonno exact button e view korbe
    expect(page.locator(".tagline")).to_contain_text("Thank you for Shopping With Us")
    context.close()

