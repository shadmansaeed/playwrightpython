from playwright.sync_api import Playwright

loginPayload = {"userEmail": "rahulshetty@gmail.com", "userPassword": "Iamking@000"}
ordersPayload = {"orders": [{"country": "India", "productOrderedId": "68a961459320a140fe1ca57a"}]}


class APIUtils:

    def getToken(self, playwright: Playwright):
        api_request_context = playwright.request.new_context(base_url="https://rahulshettyacademy.com")
        response = api_request_context.post("/api/ecom/auth/login",
                                            data=loginPayload)
        assert response.ok  # login er por 200 code je ok Dekhay setai assert kora hoise
        print(response.json())
        responseBody = response.json()  # json response ke dictionary te neya hoise
        return responseBody["token"]  # Response ke return kore dicche

    def createOrder(self, playwright: Playwright):
        token = self.getToken(playwright)  # self use kore 1 ta method ke onno method e call kora jay
        api_request_context = playwright.request.new_context(base_url="https://rahulshettyacademy.com/client")
        response = api_request_context.post("/api/ecom/order/create-order",
                                            data=ordersPayload,
                                            headers={"Authorization": token,
                                                     "Content-Type": "application/json"
                                                     })

        print(response.json())  # to print API response
