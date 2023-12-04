import allure
import requests
import random
import string


class ManageCouriers:

    @allure.step('Создаем курьера с рандомными кредами')
    def register_new_courier_random_creds_and_return_login_password(self):
        # метод генерирует строку, состоящую только из букв нижнего регистра, в качестве параметра передаём длину строки
        def generate_random_string(length):
            letters = string.ascii_lowercase
            random_string = ''.join(random.choice(letters) for i in range(length))
            return random_string

        # создаём список, чтобы метод мог его вернуть
        login_pass = []

        # генерируем логин, пароль и имя курьера
        login = generate_random_string(10)
        password = generate_random_string(10)
        first_name = generate_random_string(10)

        # собираем тело запроса
        payload = {
            "login": login,
            "password": password,
            "firstName": first_name
        }

        # отправляем запрос на регистрацию курьера и сохраняем ответ в переменную response
        response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier', data=payload)

        # если регистрация прошла успешно (код ответа 201), добавляем в список логин и пароль курьера
        if response.status_code == 201:
            login_pass.append(login)
            login_pass.append(password)
            login_pass.append(first_name)

        # возвращаем список
        return login_pass

    # === Регистрация курьера с переданными кредами ===
    def register_new_courier_pass_creds_and_return_login_password(self, payload):
        response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier', data=payload)

        return response

    @allure.step('Логинимся курьером')
    def login_courier(self, payload):
        response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/courier/login', data=payload)

        return response

    @allure.step('Удаляем курьера')
    def delete_courier(self, courier_id):
        response = requests.delete(f'https://qa-scooter.praktikum-services.ru/api/v1/courier/{courier_id}')

        return response


class ManageOrders:

    @allure.step('Создаем заказ')
    def create_order(self, payload):
        response = requests.post('https://qa-scooter.praktikum-services.ru/api/v1/orders', json=payload)

        return response

    @allure.step('Получаем список заказов')
    def get_orders_list(self):

        response = requests.get('https://qa-scooter.praktikum-services.ru/api/v1/orders')

        return response


class Checkers:

    @allure.step('Проверка ID заказа это число')
    def order_id_cheker(self, response):

        if type(response.json()['id']) == int:
            return True, 'OK'
        else:
            return False, 'Taked order_id is not integer'

    @allure.step('Проверка track заказа это число')
    def track_number_cheker(self, response):

        if type(response.json()['track']) == int:
            return True, 'OK'
        else:
            return False, 'Taked track_number is not integer'

    @allure.step('Проверяем состав и наличие значения у полей в ответе списка заказов')
    def orders_list_body_cheker(self, response):
        first_lvl_fields = ['orders', 'pageInfo', 'availableStations']
        orders_fields = ['id', 'courierId', 'firstName', 'lastName', 'address', 'metroStation', 'phone', 'rentTime',
                         'deliveryDate', 'track', 'color', 'comment', 'createdAt', 'updatedAt', 'status']
        page_info_fields = ['page', 'total', 'limit']
        available_stations_fields = ['name', 'number', 'color']

        for field_lvl_1 in first_lvl_fields:

            if field_lvl_1 in response.json():

                if field_lvl_1 == 'orders':

                    random_order_num = random.randint(0, len(response.json()['orders']) - 1)
                    for orders_fields_field in orders_fields:

                        if orders_fields_field in response.json()['orders'][random_order_num]:

                            continue

                        else:

                            raise AssertionError(f'Отсутствует поле {orders_fields_field} в orders')

                elif field_lvl_1 == 'pageInfo':

                    for page_fields_field in page_info_fields:

                        if page_fields_field in response.json()['pageInfo']:

                            continue

                        else:

                            raise AssertionError(f'Отсутствует поле {page_fields_field} в orders')

                elif field_lvl_1 == 'availableStations':

                    random_station_num = random.randint(0, len(response.json()['availableStations']) - 1)
                    for availableStations_fields_field in available_stations_fields:

                        if availableStations_fields_field in response.json()['availableStations'][random_station_num]:

                            continue

                        else:

                            raise AssertionError(f'Отсутствует поле {availableStations_fields_field} в orders')

            else:

                raise AssertionError(f'Отсутствует поле первого уровня {field_lvl_1} в ответе')

        return True

    @allure.step('Проверяем код и тело ответа')
    def status_code_and_body_checker(self, response, expected_status_code, expected_body):

        response_status_bool = response.status_code == expected_status_code
        response_body_bool = expected_body if type(expected_body) == tuple else response.json() == expected_body

        if type(expected_body) == tuple and False == (response_body_bool[0] or response_status_bool):

            raise AssertionError(f'Actual status.code {response.status_code} != expected {expected_status_code} and '
                                 f'{response_body_bool[1]}')

        elif type(expected_body) != tuple and False == (response_body_bool or response_status_bool):

            raise AssertionError(f'Actual status.code {response.status_code} != expected {expected_status_code} and '
                                 f'Actual response.json {response.json()} != expected {expected_body}')

        elif response_status_bool == False:

            raise AssertionError(f'Actual status.code {response.status_code} != expected {expected_status_code}')

        elif type(expected_body) == tuple and response_body_bool[0] == False:

            raise AssertionError(f'{response_body_bool[1]}')

        elif type(expected_body) != tuple and response_body_bool == False:

            raise AssertionError(f'Actual status.code {response.json()} != expected {expected_body}')

        else:
            return True
