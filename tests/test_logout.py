import pytest
from locators import *
from selenium.webdriver.support.ui import WebDriverWait


def test_logout(driver):
    """
    Тест проверяет возможность выхода из аккаунта.
    Предварительно необходимо авторизоваться.
    """

    # Предварительная авторизация
    email = "kiriniki999@gmail.com"
    password = "password123"

    driver.get('https://stellarburgers.nomoreparties.site/')

    # Открываем форму входа
    driver.find_element(*BUTTON_ENTER_ACCOUNT).click()

    # Вводим данные для входа
    driver.find_element(*INPUT_EMAIL).send_keys(email)
    driver.find_element(*INPUT_PASSWORD).send_keys(password)

    # Входим в аккаунт
    driver.find_element(*BUTTON_LOGIN).click()

    # Проверяем, что вошли (например, есть ссылка «Личный кабинет»)
    WebDriverWait(driver, 10).until(lambda d: d.find_element(*LINK_PERSONAL_ACCOUNT))

    # Переходим к личному кабинету
    driver.find_element(*LINK_PERSONAL_ACCOUNT).click()

    # Ждем появления кнопки выхода
    logout_button = WebDriverWait(driver, 10).until(lambda d: d.find_element(*BUTTON_LOGOUT))

    # Нажимаем кнопку "Выйти"
    logout_button.click()

    # Проверка, что пользователь вышел — например, возвращение на главную страницу или отсутствие личного кабинета
    WebDriverWait(driver, 10).until(lambda d: d.current_url.endswith('/'))

    # Или проверка наличия кнопки входа/регистрации
    assert driver.find_element(*BUTTON_ENTER_ACCOUNT).is_displayed(), "Кнопка входа не отображается после выхода"