 ![Pytest](https://img.shields.io/badge/pytest-%23ffffff.svg?style=for-the-badge&logo=pytest&logoColor=2f9fe3)
 ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
 ![Postman](https://img.shields.io/badge/Postman-FF6C37?style=for-the-badge&logo=postman&logoColor=white)

## Дипломный проект. Задание 2: Тестирование API 
***
### Автотесты для проверки ручек API приложения по заказу бургеров Stellar Burgers

### Документаия

Для просмотра описания эндпоинтов сервиса перейдите по [ссылке](https://code.s3.yandex.net/qa-automation-engineer/python-full/diploma/api-Stelar_Burger_10.25.pdf?etag=3584917d935c90b69cb3ffaff58d4f34).

### Реализованные сценарии

1. Создание пользователя:
    - создать уникального пользователя;
    - создать пользователя, который уже зарегистрирован;
    - создать пользователя и не заполнить одно из обязательных полей.
2. Логин пользователя:
    - логин под существующим пользователем,
    - логин с неверным логином и паролем.
3. Изменение данных пользователя:
    - с авторизацией,
    - без авторизации,

Для обеих ситуаций нужно проверить, что любое поле можно изменить. Для неавторизованного пользователя — ещё и то, что система вернёт ошибку.
4. Создание заказа:
    - с авторизацией,
    - без авторизации,
    - с ингредиентами,
    - без ингредиентов,
    - с неверным хешем ингредиентов.
5. Получение заказов конкретного пользователя:
    - авторизованный пользователь,
    - неавторизованный пользователь.

### Структура проекта

├───methods&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;# Папка с запросами к API эндпоинтам\
│&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;├───ingredients.py&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;# Запросы к API эндпоинту `/api/ingredients`\
│&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;├───orders.py&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;# Запросы к API эндпоинту `/api/orders`\
│&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└───users.py&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;# Запросы к API эндпоинту `/api/auth`\
│\
├───tests&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;# Папка с автотестами\
│&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;├───conftest.py&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;# Файл с фикстурами\
│&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;├───test_orders.py&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;# Тесты на проверку API эндпоинта `/api/orders` по тестовому сценарию\
│&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;└───test_users.py&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;# Тесты на проверку API эндпоинта `/api/auth` по тестовому сценарию\
│\
├───config.py&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;# Файл с константами\
├───data.py&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;# Файл с организованными данными для тестов\
├───generate_data.py&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;# Генератор данных\
├───README.md&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;# Описание проекта\
└───requirements.txt&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;# Файл с зависимостями

### Запуск автотестов

**Установка зависимостей**

> `$ pip install -r requirements.txt`

**Запуск автотестов и создание отчета о тестировании в Allure**

>  `$ pytest tests --alluredir=allure_results`

**Для формирорвания Allure отчета в формате веб-страницы**

>  `$ allure serve allure_results`

**Клонирование репозитория**

> `$ git clone https://github.com/kaithaberzus/API_tests.git`



