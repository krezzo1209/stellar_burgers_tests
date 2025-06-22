from selenium.webdriver.common.by import By

# Заголовки страниц
HEADER_TITLE = (By.TAG_NAME, 'h1')

# Главная страница
BUTTON_ENTER_ACCOUNT = (By.XPATH, "//button[contains(text(), 'Войти в аккаунт')]")
LOGO_STELLAR_BURGERS = (By.CSS_SELECTOR, ".AppHeader_header__logo__2D0X2")

# Форма входа / регистрации / восстановления пароля
INPUT_EMAIL = (By.NAME, 'email')
INPUT_PASSWORD = (By.NAME, 'password')
INPUT_NAME = (By.NAME, 'name')

BUTTON_LOGIN = (By.XPATH, "//button[contains(text(), 'Войти')]")
BUTTON_REGISTER = (By.XPATH, "//button[contains(text(), 'Зарегистрироваться')]")
BUTTON_FORGOT_PASSWORD = (By.XPATH, "//button[contains(text(), 'Восстановить пароль')]")
BUTTON_SUBMIT_FORGOT_PASSWORD = (By.XPATH, "//button[contains(text(), 'Восстановить')]")  # если есть

# Личный кабинет и выход
LINK_PERSONAL_ACCOUNT = (By.XPATH, "//a[contains(@href, '/account') and contains(text(), 'Личный Кабинет')]")
BUTTON_LOGOUT = (By.XPATH, "//button[contains(text(), 'Выйти')]")

# Вкладки конструктора
TAB_BUNS = (By.XPATH, "//div[text()='Булки']")
TAB_SAUCES = (By.XPATH, "//div[text()='Соусы']")
TAB_FILLINGS = (By.XPATH, "//div[text()='Начинки']")

# Навигация внутри сайта
CONSTRUCTOR_LINK = (By.XPATH, "//a[contains(@href, '/') and contains(text(), 'Конструктор')]")
LOGO_LINK = LOGO_STELLAR_BURGERS

