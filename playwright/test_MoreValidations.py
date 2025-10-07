import time

from playwright.sync_api import Page, expect


def test_UIChecks(page: Page):
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")

    expect(page.get_by_placeholder("Hide/Show Example")).to_be_visible()  # placeholder
    time.sleep(2)
    page.get_by_role("button", name="Hide").click()
    expect(page.get_by_placeholder("Hide/Show Example")).to_be_hidden()
    time.sleep(5)


