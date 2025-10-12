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


# child page operation
# not working (questioned at course teacher)
def test_childWindowHandle(page: Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")

    with page.expect_popup() as newPage_info:
        page.locator(".blinkingText").click()  # new page
        childPage = newPage_info.value
        text = childPage.locator(".red").text_content()  # validate child window is working or not
        print(text)


# working childwindow
def test_childWindowHandle(page: Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")

    # manually force open in new tab using JS
    with page.context.expect_page() as newPage_info:
        page.evaluate("window.open(document.querySelector('.blinkingText').href, '_blank')")
    childPage = newPage_info.value

    text = childPage.locator(".red").text_content()
    print(text)  # Please email us at mentor@rahulshettyacademy.com with below template to receive response
    words = text.split("at")  # 0  -> Please email us  1 -> mentor@rahulshettyacademy.com with below template to receive response
    email = words[1].strip().split(" ")[0]  # (space er opor depend kore index korse) 0 -> mentor@rahulshettyacademy.com 1 ->
    assert email == "mentor@rahulshettyacademy.com"




# Got answer from my UDEMY question, trainer give me this code
def test_child_window_practice(page: Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    # expect_popup() is the keyword which will fetch new window and store it in a vairbale - new_page_info
    with page.expect_popup() as new_page_info:
        page.get_by_role("link", name="Free Access to InterviewQues/ResumeAssistance/Material").click()
        child_window = new_page_info.value  # It will get the new window instance
        text = child_window.locator(".red").text_content()  # text_content() to extract text from the locator
        print(text)
        word = text.split("at")
        email_id = word[1].strip().split(" ")[0]
        assert email_id == "mentor@rahulshettyacademy.com"
