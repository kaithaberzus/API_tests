from faker import Faker


class GenerateData:

    fake_en = Faker()

    #Генерация имени
    def create_name(self):
        return self.fake_en.name()

    #Генерация пароля
    def create_password(self):
        return self.fake_en.password()

    #Генерация почты
    def create_email(self):
        return self.fake_en.email()