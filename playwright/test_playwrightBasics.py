from playwright.sync_api import Page  # To get suggestion of different actions
import time


def test_playwrightBasics(playwright):
    browser = playwright.chromium.launch(headless=False)   # chrome  and EDGE browser
    context = browser.new_context()   # open browser in incognito
    page = context.new_page()  # open incognito page
    page.goto("https://rahulshettyacademy.com")
    time.sleep(4)


# page is used in chromium headless mode, 1 single context
def test_playwrightShortcut(page: Page):   # modify run configuration "--headed" to run in browser
    page.goto("https://rahulshettyacademy.com")  # pytest test_playwrightBasics.py::test_playwrightShortcut --headed


# CSS SELECTOR 1. #terms(for id)  2 .text-info(for class name)
def test_coreLocators(page: Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label("Username:").fill("rahulshettyacademy")  # input username
    page.get_by_label("Password:").fill("learning")  # password
    page.get_by_role("combobox").select_option("teach")  # select dropdown
    page.locator("#terms").check()  # check the checkbox with CSS selector
    page.get_by_role("link", name="terms and conditions").click()  # clicking terms and condition
    page.get_by_role("button", name="Sign In").click()  # click on button

    time.sleep(10)


