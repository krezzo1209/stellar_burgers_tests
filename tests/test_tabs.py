import pytest
from locators import *


def test_tabs_switching(driver):
    """
     Проверка переключения вкладок «Булки», «Соусы», «Начинки».
     """

    url_base = 'https://stellarburgers.nomoreparties.site/'
    driver.get(url_base)

    tabs_locators_and_names = [
        (TAB_BUNS, 'Булки'),
        (TAB_SAUCES, 'Соусы'),
        (TAB_FILLINGS, 'Начинки')
    ]

    for locator, name in tabs_locators_and_names:
        tab_elem = None
        try:
            tab_elem = driver.find_element(*locator)
            tab_elem.click()
            header_title_elem = None

            header_title_elem = WebDriverWait(driver, 10).until(
                lambda d: d.find_element(By.TAG_NAME, 'h1')
            )

            assert header_title_elem.text == name or name in header_title_elem.text

        except Exception as e:
            pytest.fail(f"Ошибка при переключении на вкладку {name}: {e}")