from pages.base_page import BasePage
from locators.login_page_locators import LoginPageLocators as LPLocs
from urls import Url
import allure


class LoginPage(BasePage):

    @allure.step('Открываем страницу авторизации')
    def open_login_page(self):
        self.go_to_page(Url.LOGIN_PAGE)

    @allure.step('Ожидание загрузки страницы авторизации')
    def wait_load_login_page(self):
        self.wait_for_visibility_element(LPLocs.LOGIN_PAGE_HEADER)

    @allure.step('Заполняем поле "Email"')
    def set_email_placeholder(self, email):
        self.set_data(LPLocs.FIELD_EMAIL, email)

    @allure.step('Заполняем поле "Пароль"')
    def set_password_placeholder(self, password):
        self.set_data(LPLocs.FIELD_PASSWORD, password)

    @allure.step('Нажимаем кнопку "Войти"')
    def click_button_enter(self):
        self.click_on_element(LPLocs.BUTTON_LOGIN)

    @allure.step('Авторизация пользователя')
    @allure.description('Переход на страницу авторизации с ожиданием её загрузки, ' \
    'и авторизация пользователя')
    def user_login(self, email, password):
        self.open_login_page()
        self.wait_load_login_page()
        self.set_email_placeholder(email)
        self.set_password_placeholder(password)
        self.click_button_enter()
