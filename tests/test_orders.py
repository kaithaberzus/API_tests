from methods.orders import Orders
from data import *
from methods.ingredients import Ingredients
import allure


class TestOrders(Orders):

    data = CompleteData()
    message = TextMessage()
    ing = Ingredients()

    @allure.title('Проверка статус кода и текста ответа при создании заказа с авторизацией и переданными хэшами')
    def test_create_order_with_auth_and_ingr(self, delete_user):
        create_order = self.create_order(self.data.body_create_order(self.ing.get_ing_id()), delete_user[2])

        assert (create_order[0].get("success") == True
                and create_order[0].get("name") == 'Флюоресцентный бургер'
                and create_order[1] == 200), \
            "Заказ не создан"

    @allure.title('Проверка кода и текста ответа при создании заказа без авторизации')
    def test_create_order_without_auth(self, delete_user):
        create_order = self.create_order(self.data.body_create_order(self.ing.get_ing_id()), None)

        assert (create_order[0]['success'] == True
                and create_order[1] == 200), \
            "Заказ не создан"

    @allure.title('Проверка кода и текста ответа при создании заказа без ингредиентов')
    def test_create_order_without_ingr(self, delete_user):
        create_order = self.create_order(self.data.body_create_order(''), delete_user[2])

        assert (create_order[0]['success'] == False
                and create_order[0]['message'] == self.message.no_ingredient
                and create_order[1] == 400)

    @allure.title('Проверка кода и текста ответа при создании заказа с неверным хэшем')
    def test_create_order_with_false_order_id(self, delete_user):
        create_order = self.create_order(self.data.body_create_order('61c0c5a71d1f088005553535'), delete_user[2])

        assert create_order[1] == 400 and create_order[0]['success'] == False

    @allure.title('Проверка кода и текста ответа при получении списка заказов пользователя без авторизации')
    def test_get_order_with_auth(self, delete_user):
        get_orders = self.get_order(delete_user[2])

        assert ('orders' in get_orders[0]
                and get_orders[1] == 200), \
            "Заказы пользователя не получены"

    @allure.title('Проверка кода и текста ответа при получении списка заказов пользователя с авторизацией')
    def test_get_order_without_auth(self):
        get_orders = self.get_order(None)

        assert (get_orders[0]['message'] == self.message.no_auth
                and get_orders[1] ==401)
