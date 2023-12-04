from helpers.helpers import ManageCouriers, Checkers
from helpers.constants import Constants
import pytest


class TestCreateCourier:

    m_couriers = ManageCouriers()
    const = Constants()
    payload = const.COURIERS
    checker = Checkers()
    def test_create_courier_success(self):

        response = self.m_couriers.register_new_courier_pass_creds_and_return_login_password(self.payload['valid'][0])

        assert self.checker.status_code_and_body_checker(response=response,
                                                                 expected_status_code=201,
                                                                 expected_body={'ok': True}
                                                                 )


    def test_create_already_exist_courier_error(self):

        response1 = self.m_couriers.register_new_courier_pass_creds_and_return_login_password(self.payload['valid'][1])
        response2 = self.m_couriers.register_new_courier_pass_creds_and_return_login_password(self.payload['valid'][1])

        assert self.checker.status_code_and_body_checker(response=response2,
                                                         expected_status_code=409,
                                                         expected_body={'code': 409, 'message':
                                                             'Этот логин уже используется. Попробуйте другой.'}
                                                         )

    @pytest.mark.parametrize("payload", payload['without_mandatory'])
    def test_create_courier_without_mandatory_field_error(self, payload):

        response = self.m_couriers.register_new_courier_pass_creds_and_return_login_password(payload)

        assert self.checker.status_code_and_body_checker(response=response,
                                                         expected_status_code=400,
                                                         expected_body={'code': 400, 'message':
                                                             'Недостаточно данных для создания учетной записи'}
                                                         )

    @classmethod
    def teardown_class(cls):

        response1 = cls.m_couriers.login_courier(cls.payload['valid'][0])
        response2 = cls.m_couriers.login_courier(cls.payload['valid'][1])

        cls.m_couriers.delete_courier(response1.json()['id'])
        cls.m_couriers.delete_courier(response2.json()['id'])
