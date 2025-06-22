import pytest
from locators import *


def test_personal_account_link(driver):


    # Предварительно авторизуемся:

    email = "existing_user@yandex.ru"
    password = "password123"

    driver.get('https://stellarburgers.nomoreparties.site/')
    driver.find_element(*BUTTON_ENTER_ACCOUNT).click()
    driver.find_element(*INPUT_EMAIL).send_keys(email)
    driver.find_element(*INPUT_PASSWORD).send_keys(password)
    driver.find_element(*BUTTON_LOGIN).click()

    # Переход по ссылке «Личный кабинет»
    link_account = driver.find_element(*LINK_PERSONAL_ACCOUNT)
    link_account.click()

    assert "/account" in driver.current_url or \
           any(elem.is_displayed() for elem in [driver.find_element(By.TAG_NAME, 'h2')])  # пример проверки


def test_logo_redirect_to_main(driver):
    """
      Проверка перехода по логотипу на главную страницу.
      """



    logo_elem = None

    try:
        logo_elem = driver.find_element(*LOGO_STELLAR_BURGERS)
        logo_elem.click()

        assert "/main" in driver.current_url or \
               any(elem.is_displayed() for elem in [driver.find_element(By.TAG_NAME, 'h1')])

    except Exception as e:
        pytest.fail(f"Не удалось найти логотип: {e}")