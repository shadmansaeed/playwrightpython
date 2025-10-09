import time

from playwright.sync_api import Page, expect


def test_UIChecks(page: Page):
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")

    expect(page.get_by_placeholder("Hide/Show Example")).to_be_visible()  # placeholder
    time.sleep(2)
    page.get_by_role("button", name="Hide").click()
    expect(page.get_by_placeholder("Hide/Show Example")).to_be_hidden()
    time.sleep(2)



    #AlertBoxes
    page.on("dialog", lambda dialog: dialog.accept())  # dialog box asle jeno accept korte pare eijonno use kora hoise
    page.get_by_role("button", name="Confirm").click()  # oneliner function(anonymous functions are used as lambda)
    time.sleep(3)

    # FrameHandling
    pageFrame = page.frame_locator("#courses-iframe")
    pageFrame.get_by_role("link", name="All Access plan").click()
    expect(pageFrame.locator("body")).to_contain_text("Happy Subscibers!")




