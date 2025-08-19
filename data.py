from generate_data import *


class CompleteData:

    generate = GenerateData()

    #Создание тела запроса с данными заказа
    def body_create_order(self, ingredient):
        ingredients = {
            "ingredients": [f'{ingredient}']
                       }
        return ingredients

    #Создание тела запроса с данными пользователя без пароля
    def false_body_create_user(self):
        user_data = {"email": self.generate.create_email(),
                     "name": self.generate.create_name()
                     }
        return user_data

    #Создание тела запроса с данными пользователя
    def body_create_user(self):
        user_data = {"email": self.generate.create_email(),
                     "password": self.generate.create_password(),
                     "name": self.generate.create_name()
                     }
        return user_data

    #Хэдер
    @staticmethod
    def header(token):
        return {"Authorization": f"{token}"}

#Класс с текстами ответа
class TextMessage:

    user_exists = "User already exists"
    no_field = "Email, password and name are required fields"
    incorrect_password_or_login = "email or password are incorrect"
    no_auth = "You should be authorised"
    no_ingredient = "Ingredient ids must be provided"
