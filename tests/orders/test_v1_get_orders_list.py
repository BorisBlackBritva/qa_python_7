from helpers.helpers import ManageOrders, Checkers


class TestGetOrdersList:

    m_orders = ManageOrders()
    checker = Checkers()

    def test_get_orders_list_success(self):

        response = self.m_orders.get_orders_list()

        assert self.checker.orders_list_body_cheker(response)
