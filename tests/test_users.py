from methods.users import User
from data import *
import allure


class TestUser(User):

    data = CompleteData()
    message = TextMessage()

    @allure.title('Проверка кода и текста ответа при создании пользователя с валидными данными')
    def test_create_user_true(self):
        user = self.create_user(self.data.body_create_user())

        assert (user[0]['success'] == True
                and 'accessToken' in user[0]
                and user[1] == 200)
        self.delete_user(user[2]), \
            "Пользователь не создан"

    @allure.title('Проверка кода и текста ответа при создании пользователя без пароля')
    def test_create_user_no_password(self):
        user = self.create_user(self.data.false_body_create_user())

        assert (user[0]['message'] == self.message.no_field
                and user[1] == 403)

    @allure.title('Проверка проверка кода и текста ответа при создании двух одинаковых пользователей')
    def test_create_user_same_data(self, delete_user):
        user_double = self.create_user(delete_user[3])

        assert (user_double[0]['message'] == self.message.user_exists
                and user_double[1] == 403)

    @allure.title('Проверка кода и текста ответа при логине существующего пользователя')
    def test_login_user_true(self, delete_user):
        login = self.login_user(delete_user[3])

        assert (login[0]['success'] == True
                and 'accessToken' in login[0]
                and login[1] == 200), \
            "Пользователь не залогинен"

    @allure.title('Проверка кода и текста ответа при логине пользователя без пароля')
    def test_login_user_no_password(self):
        login = self.login_user(self.data.false_body_create_user())

        assert (login[0]['message'] == self.message.incorrect_password_or_login
                and login[1] == 401)

    @allure.title('Проверка кода и текста ответа при обновлении данных пользователя с авторизации')
    def test_update_user_data_with_auth(self, delete_user):
        new_data = self.data.body_create_user()
        update = self.update_user_data(new_data, delete_user[2])

        assert (update[0]['success'] == True
                and update[0]['user']['email'] == new_data['email']
                and update[0]['user']['name'] == new_data['name']
                and update[1] == 200), \
            "Данные не обновились"

    @allure.title('Проверка кода и текста ответа при обновлении данных пользователя без авторизацией')
    def test_update_user_without_auth(self):
        update = self.update_user_data(self.data.body_create_user(), '')

        assert (update[0]['success'] == False
                and update[1] == 401)