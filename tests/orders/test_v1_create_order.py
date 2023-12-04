from helpers.helpers import ManageOrders, Checkers
from helpers.constants import Constants
import pytest


class TestCreateOrder:

    m_orders = ManageOrders()
    const = Constants()
    checker = Checkers()

    @pytest.mark.parametrize('payload', const.ORDERS)
    def test_create_order(self, payload):

        #payload = json.dumps(payload)
        response = self.m_orders.create_order(payload)

        assert self.checker.status_code_and_body_checker(response=response,
                                                         expected_status_code=201,
                                                         expected_body=self.checker.track_number_cheker(response)
                                                         )
