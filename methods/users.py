from json import JSONDecoder

import requests
from requests import JSONDecodeError

import config
from data import CompleteData
import allure


class User:

    @allure.step('Удаление аккаунта пользователя')
    def delete_user(self, token):
        delete = requests.delete(f"{config.BASE_URL}{config.USER_URL}/user",
                                 headers=CompleteData.header(token)
                                 )

        return delete

    @allure.step('Создание аккаунта пользователя')
    def create_user(self, data):
        registration = requests.post(f"{config.BASE_URL}{config.USER_URL}/register",
                                     data=data
                                     )
        access_token = registration.json().get('accessToken')

        return registration.json(), registration.status_code, access_token

    @allure.step('Логин пользователя')
    def login_user(self, data):
        login = requests.post(f"{config.BASE_URL}{config.USER_URL}/login",
                              data=data
                              )
        access_token = login.json().get("accessToken")

        return login.json(), login.status_code, access_token

    @allure.step('Обновление данных пользователя')
    def update_user_data(self, data, token):
        new_user_data = requests.patch(f'{config.BASE_URL}{config.USER_URL}/user',
                                       data=data,
                                       headers=CompleteData.header(token)
                                       )

        return new_user_data.json(), new_user_data.status_code
