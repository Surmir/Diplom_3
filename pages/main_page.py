from pages.base_page import BasePage
from locators.base_page_locators import BasePageLocators as BPLocs
from locators.main_page_locators import MainPageLocators as MPLocs
from urls import Url
import allure


class MainPage(BasePage):

    @allure.step('Открываем главную страницу')
    def open_main_page(self):
        self.go_to_page(Url.MAIN_PAGE)

    @allure.step('Ожидание загрузки главной страницы')
    def wait_load_main_page(self):
        self.wait_for_visibility_element(MPLocs.MAIN_PAGE_HEADER)

    @allure.step('Нажимаем на кнопку "Лента Заказов" в шапке страницы')
    def click_button_feed(self):
        self.click_on_element(BPLocs.HEADER_BUTTON_FEED)

    @allure.step('Проверяем переход на страницу "Лента Заказов"')
    def check_open_feed_page(self):
        actual_url = self.get_page_url()
        expect_url = Url.FEED_PAGE
        return actual_url == expect_url

    @allure.step('Нажимаем на ингредиент')
    def click_ingredient(self):
        self.click_on_element(MPLocs.INGREDIENT)

    @allure.step('Ожидаем появления окна "Детали ингредиента"')
    def wait_load_window_ingred_details(self):
        self.wait_for_visibility_element(MPLocs.WINDOW_INGR_DETAILS)

    @allure.step('Проверяем появление окна "Детали ингредиента"')
    def check_open_window_ingred_details(self):
        return self.check_element_is_displayed(MPLocs.WINDOW_INGR_DETAILS)

    @allure.step('Нажимаем на кнопку "Х" в окне "Детали ингредиента"')
    def click_button_x(self):
        self.click_on_element(MPLocs.BUTTON_CLOSE_X)

    @allure.step('Добавляем ингредиент в заказ')
    def add_ingredient_to_order(self):
        self.drag_and_drop_element(MPLocs.INGREDIENT, MPLocs.BURGER_CONSTRUCTOR)

    @allure.step('Проверяем счетчик ингредиента')
    def check_counter_ingredient(self):
        count = self.get_text(MPLocs.COUNTER_INGREDIENT)
        return int(count)
    
    @allure.step('Нажимаем на кнопку "Оформить заказ"')
    def click_button_create_order(self):
        self.click_on_element(MPLocs.BUTTON_CREATE_ORDER)

    @allure.step('Ожидаем появления окна id заказа')
    def wait_load_window_order_details(self):
        self.wait_for_visibility_element(MPLocs.ID_ORDER, 3)

    @allure.step('Получаем id заказа')
    def get_id_order(self):
        return self.get_text(MPLocs.ID_ORDER)
    
    @allure.step('Создаем заказ')
    def create_order(self):
        self.add_ingredient_to_order()
        self.click_button_create_order()
