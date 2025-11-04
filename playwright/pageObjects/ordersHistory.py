from .orderDetails import OrderDetailsPage


class OrdersHistoryPage:


    def __init__(self,page):
        self.page =page


    def selectOrder(self, orderId):
        row = self.page.locator("tr").filter(has_text=orderId)  # orderid dile exact orderid khuje pabe
        row.get_by_role("button", name="View").click()  # ekhane row. use korar jonno exact button e view korbe

        orderDetailsPage= OrderDetailsPage(self.page)
        return orderDetailsPage







