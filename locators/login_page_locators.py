from selenium.webdriver.common.by import By


class LoginPageLocators():
    #заголовок страницы авторизации
    LOGIN_PAGE = (By.XPATH, ".//h2[text()='Вход']")
    #поле email
    FIELD_EMAIL = (By.XPATH, ".//input[@name='name']")
    #поле пароль
    FIELD_PASSWORD = (By.XPATH, ".//input[@name='Пароль']")
    #кнопка'Войти'
    BUTTON_LOGIN = (By.XPATH, ".//button[text()='Войти']")
