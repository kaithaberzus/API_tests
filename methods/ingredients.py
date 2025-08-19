import config
import requests
import allure


class Ingredients:

    @allure.step('Получение хэша ингредиента')
    def get_ing_id(self):
        ing_data = requests.get(f"{config.BASE_URL}{config.ING_URL}")
        return ing_data.json()['data'][0]['_id']