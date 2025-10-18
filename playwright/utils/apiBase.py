from playwright.sync_api import Playwright


class APIUtils:

    def createOrder(self,playwright:Playwright):
        api_request_context = playwright.request.new_context(base_url="https://rahulshettyacademy.com/client")
        api_request_context
