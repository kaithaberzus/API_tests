import pytest
from methods.users import User
from data import *


# Фикстура удаления пользователя
@pytest.fixture
def delete_user():
    user = User()
    data = CompleteData()

    user_data = data.body_create_user()
    registration = user.create_user(user_data)

    yield registration[0], registration[1], registration[2], user_data

    user.delete_user(registration[2])