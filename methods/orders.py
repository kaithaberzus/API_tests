import config
import requests
import allure
from data import CompleteData


class Orders:

    @allure.step('Создание заказа')
    def create_order(self, data, token):
        post_order = requests.post(f"{config.BASE_URL}{config.ORDER_URL}",
                                   data=data,
                                   headers=CompleteData.header(token)
                                   )

        return post_order.json(), post_order.status_code

    @allure.step('Получение список заказов пользователя')
    def get_order(self, token):
        get_order = requests.get(f"{config.BASE_URL}{config.ORDER_URL}",
                                 headers=CompleteData.header(token)
                                 )

        return get_order.json(), get_order.status_code