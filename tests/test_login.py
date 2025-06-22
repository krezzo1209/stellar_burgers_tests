def test_successful_login(driver):
    """
     Тест успешного входа по зарегистрированным данным.
     """

    email = "kiriniki999@gmail.com"
    password = "яусталa"

    driver.get('https://stellarburgers.nomoreparties.site/')

    # Открываем форму входа
    driver.find_element(*BUTTON_ENTER_ACCOUNT).click()

    # Вводим данные
    driver.find_element(*INPUT_EMAIL).send_keys(email)
    driver.find_element(*INPUT_PASSWORD).send_keys(password)

    # Нажимаем войти
    driver.find_element(*BUTTON_SUBMIT).click()

    # Проверка перехода в личный кабинет или наличие элемента личного кабинета
    assert "Личный кабинет" in driver.page_source or \
           "account" in driver.current_url or \
           len(driver.find_elements(By.XPATH, "//a[contains(@href,'account')]")) > 0

