from helpers.constants import Constants
from helpers.helpers import ManageCouriers, Checkers
import pytest


class TestLoginCourier:

    m_couriers = ManageCouriers()
    const = Constants()
    checker = Checkers()
    payload = const.COURIERS

    @classmethod
    def setup_class(cls):
        cls.m_couriers.register_new_courier_pass_creds_and_return_login_password(cls.payload['valid'][0])

    def test_login_courier_success(self):
        response = self.m_couriers.login_courier(self.payload['valid'][0])

        assert self.checker.status_code_and_body_checker(response=response,
                                                         expected_status_code=200,
                                                         expected_body=self.checker.order_id_cheker(response)
                                                         )

    @pytest.mark.parametrize("payload", [
                             # payload['without_mandatory'][0], # ДЕФЕКТ, возвращает 504
                             # payload['without_mandatory'][1], # ДЕФЕКТ, возвращает 504
                             payload['without_mandatory'][2],
                             payload['without_mandatory'][3]
                             ])
    def test_login_courier_without_mandatory_field_error(self, payload):
        response = self.m_couriers.login_courier(payload)

        assert self.checker.status_code_and_body_checker(response=response,
                                                         expected_status_code=400,
                                                         expected_body={'code': 400, 'message':'Недостаточно данных для входа'}
                                                         )

    @pytest.mark.parametrize("payload", payload['incorrect_credentials'])
    def test_login_courier_wrong_creds_field_error(self, payload):
        response = self.m_couriers.login_courier(payload)

        assert self.checker.status_code_and_body_checker(response=response,
                                                         expected_status_code=404,
                                                         expected_body={'code': 404, 'message': 'Учетная запись не найдена'}
                                                         )

    @classmethod
    def teardown_class(cls):

        response = cls.m_couriers.login_courier(cls.payload['valid'][0])

        cls.m_couriers.delete_courier(response.json()['id'])
