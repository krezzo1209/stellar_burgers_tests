import pytest
from selenium import webdriver

@pytest.fixture(scope='function')
def driver():
    driver = webdriver.Chrome()  # Убедитесь, что ChromeDriver установлен и в PATH
    driver.maximize_window()
    yield driver
    driver.quit()