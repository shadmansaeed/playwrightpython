import time

from playwright.sync_api import Page, expect


def test_UIValidationDynamicScript(page: Page):
    # iphone x, nokia edge -> verify 2 items are showing in cart
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label("Username:").fill("rahulshettyacademy")  # input username
    page.get_by_label("Password:").fill("learning")  # password
    page.get_by_role("combobox").select_option("teach")  # select dropdown
    page.locator("#terms").check()  # check the checkbox with CSS selector
    page.get_by_role("button", name="Sign In").click()  # click on button
    # app-card holo tagname, filter kortese iphone ke( 4tar moddhe)
    iphoneProduct = page.locator("app-card").filter(has_text="iphone X")
    # iphoneProduct only iphone product er moddhei simaboddho, full page scan korena
    iphoneProduct.get_by_role("button").click()

    nokiaProduct = page.locator("app-card").filter(has_text="Nokia Edge")
    # nokiaProduct only iphone product er moddhei simaboddho, full page scan korena
    nokiaProduct.get_by_role("button").click()
    page.get_by_text("Checkout").click()  # partial text supports

    expect(page.locator(".media-body")).to_have_count(2)  # 2 ta product validate korbe
    time.sleep(10)
