import os
import json
import pytest
from playwright.sync_api import Playwright, expect

from pageObjects.login import LoginPage
from pageObjects.dashboard import DashboardPage
from utils.apiBase1 import APIUtils

# ---------- JSON PATH FIX ✔ ----------
# Get absolute path of this test file
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Go to: /playwright/data/credentials.json
json_path = os.path.join(BASE_DIR, "data", "credentials.json")

with open(json_path, 'r') as f:
    test_data = json.load(f)
    user_credentials_list = test_data["user_credentials"]


@pytest.mark.parametrize('user_credentials', user_credentials_list)
def test_e2e_web_api(playwright: Playwright,browserInstance,user_credentials):
    userName = user_credentials["userEmail"]
    Password = user_credentials["userPassword"]

    #browser = playwright.chromium.launch(False)
    #context = browser.new_context()
    #page = context.new_page()

    # Create order --> orderID
    api_utils = APIUtils()
    orderId = api_utils.createOrder(playwright, user_credentials)

    # Login
    loginPage = LoginPage(browserInstance)
    loginPage.navigate()
    dashboardPage = loginPage.login(userName, Password)

    # Dashboard Page
    orderHistoryPage = dashboardPage.selectOrdersNavLink()
    ordersDetailsPage = orderHistoryPage.selectOrder(orderId)
    ordersDetailsPage.verifyOrderMessage()

    #context.close()
