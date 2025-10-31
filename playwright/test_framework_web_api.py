import json

import pytest
from playwright.sync_api import Playwright, expect

from utils.apiBase import APIUtils

# Json file ->util->access into test

with open('data/credentials.json') as f:  # reference stored in f
    test_data = json.load(f)  # load method convert json file into python object
    print(test_data)
    user_credentials_list = test_data['user_credentials']


@pytest.mark.parametrize('user_credentials', user_credentials_list)  # everytime pull 1 time for test # here user_credential is only a parameter
def test_e2e_web_api(playwright: Playwright, user_credentials):  # here user_credential is a fixture
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    # create order --> orderID

    api_Utils = APIUtils()
    orderId = api_Utils.createOrder(playwright, user_credentials)

    # login
    page.goto("https://rahulshettyacademy.com/client")
    page.get_by_placeholder("email@example.com").fill(user_credentials["userEmail"])
    page.get_by_placeholder("enter your passsword").fill(user_credentials["userPassword"])
    page.get_by_role("button", name="Login").click()

    # Click on Orders
    page.get_by_role("button", name="ORDERS").click()

    # orders history page --> order is present
    #row = page.locator("tr").filter(has_text=orderId)  # orderid dile exact orderid khuje pabe
    #row.get_by_role("button", name="View").click()  # ekhane row. use korar jonno exact button e view korbe
    #expect(page.locator(".tagline")).to_contain_text("Thank you for Shopping With Us")
    #context.close()
