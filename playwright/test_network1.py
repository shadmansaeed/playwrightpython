import time

from playwright.sync_api import Page

fakePayloadOrderResponse = {"data":[],"message":"No Orders"}

#-> api call from browser--> api call contact server return back response to browser--> browser use response to generate html

def intercept_response(route):
    route.fulfill(
        json = fakePayloadOrderResponse
    )

def test_Network_1(page : Page):
    # login
    page.goto("https://rahulshettyacademy.com/client")
    time.sleep(2)
    page.route("https://rahulshettyacademy.com/api/ecom/order/get-orders-for-customer/*", intercept_response)
    time.sleep(2)
    page.get_by_placeholder("email@example.com").fill("rahulshetty@gmail.com")
    time.sleep(2)
    page.get_by_placeholder("enter your passsword").fill("Iamking@000")
    time.sleep(2)
    page.get_by_role("button", name="Login").click()
    time.sleep(3)

    # Click on Orders
    page.get_by_role("button", name="ORDERS").click()

    time.sleep(4)


    order_text= page.locator(".mt-4").text_content()  # you have no order" oi place e css selector diye neya
    print(order_text)




