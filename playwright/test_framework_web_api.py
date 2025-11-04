import json

import pytest
from playwright.sync_api import Playwright, expect

from pageObjects.login import LoginPage
from pageObjects.dashboard import DashboardPage
from utils.apiBase1 import APIUtils

# Json file ->util->access into test

with open('playwright/data/credentials.json') as f:  # reference stored in f   #playwright/data/credentials.json   'data/credentials.json'
    test_data = json.load(f)  # load method convert json file into python object
    print(test_data)
    user_credentials_list = test_data['user_credentials']


@pytest.mark.parametrize('user_credentials', user_credentials_list)  # everytime pull 1 time for test # here user_credential is only a parameter
def test_e2e_web_api(playwright: Playwright, user_credentials):  # here user_credential is a fixture
    userName= user_credentials["userEmail"]
    Password = user_credentials["userPassword"]
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    # create order --> orderID

    api_Utils = APIUtils()
    orderId = api_Utils.createOrder(playwright, user_credentials)

    # login
    loginPage = LoginPage(page)  # object for login page class
    loginPage.navigate()
    dashboardPage= loginPage.login(userName,Password)

    #Dashboard Page
    #dashboardPage= DashboardPage(page)
    orderHistoryPage= dashboardPage.selectOrdersNavLink()
    ordersDetailsPage= orderHistoryPage.selectOrder(orderId)
    ordersDetailsPage.verifyOrderMessage()
    context.close()

    # Click on Orders
    #page.get_by_role("button", name="ORDERS").click()

    # orders history page --> order is present
    #row = page.locator("tr").filter(has_text=orderId)  # orderid dile exact orderid khuje pabe
    #row.get_by_role("button", name="View").click()  # ekhane row. use korar jonno exact button e view korbe
    #expect(page.locator(".tagline")).to_contain_text("Thank you for Shopping With Us")
    #
