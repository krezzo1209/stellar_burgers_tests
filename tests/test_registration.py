import pytest
from locators import *
from utils import generate_email, generate_password


def test_successful_registration(driver):
    driver.get('https://stellarburgers.nomoreparties.site/')

    # Открываем форму входа/регистрации
    driver.find_element(*BUTTON_ENTER_ACCOUNT).click()



    email = generate_email('testuser')
    password = generate_password(8)

    driver.find_element(*INPUT_NAME).send_keys('Тестовый Пользователь')
    driver.find_element(*INPUT_EMAIL).send_keys(email)
    driver.find_element(*INPUT_PASSWORD).send_keys(password)

    # Нажимаем кнопку "Зарегистрироваться"
    driver.find_element(*BUTTON_REGISTER).click()

    # Проверка успешной регистрации
    assert "account" in driver.current_url or \
           driver.find_element(*LINK_PERSONAL_ACCOUNT).is_displayed()


def test_registration_with_short_password(driver):
    driver.get('https://stellarburgers.nomoreparties.site/')

    driver.find_element(*BUTTON_ENTER_ACCOUNT).click()

    email = generate_email('testuser')

    short_password = '12345'  # менее 6 символов

    driver.find_element(*INPUT_NAME).send_keys('Тест')
    driver.find_element(*INPUT_EMAIL).send_keys(email)
    driver.find_element(*INPUT_PASSWORD).send_keys(short_password)

    # Пытаемся зарегистрироваться с коротким паролем и проверяем сообщение об ошибке.

    driver.find_element(*BUTTON_REGISTER).click()

    # Предположим есть сообщение об ошибке:
    error_locator = (By.CSS_SELECTOR, ".input__error")  # пример локатора ошибки

    error_elements = driver.find_elements(*error_locator)

    assert any("минимум из шести символов" in e.text.lower() for e in error_elements), \
        "Ошибка о минимальной длине пароля не отображается"