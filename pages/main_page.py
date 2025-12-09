from pages.base_page import BasePage
from locators.base_page_locators import BasePageLocators as BPLocs
from locators.main_page_locators import MainPageLocators as MPLocs
from data import TestWaitTime as TWTime
from urls import Url
import allure


class MainPage(BasePage):

    @allure.step('Открываем главную страницу')
    def open_main_page(self):
        self.go_to_page(Url.MAIN_PAGE)

    @allure.step('Ожидание загрузки главной страницы')
    def wait_load_main_page(self, wait_time=TWTime.PAGE):
        self.wait_for_visibility_element(MPLocs.MAIN_PAGE_HEADER, wait_time)

    @allure.step('Открываем главную страницу и ожидаем её загрузки')
    def wait_open_and_load_main_page(self, wait_time=TWTime.PAGE):
        self.open_main_page()
        self.wait_load_main_page(wait_time)

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

    @allure.step('Проверяем появление окна "Детали ингредиента"')
    def check_open_window_ingred_details(self, wait_time=TWTime.WINDOW):
        return self.check_element_is_displayed(MPLocs.WINDOW_INGR_DETAILS, wait_time)

    @allure.step('Проверяем закрытие окна "Детали ингредиента"')
    def check_close_window_ingred_details(self, wait_time=TWTime.INVISIBLE):
        return self.check_element_not_is_displayed(MPLocs.WINDOW_INGR_DETAILS, wait_time)

    @allure.step('Нажимаем на кнопку "Х" в окне "Детали ингредиента"')
    def click_button_x(self):
        self.click_on_element(MPLocs.BUTTON_CLOSE_X)

    @allure.step('Добавляем ингредиент в заказ')
    def add_ingredient_to_order(self):
        self.drag_and_drop_element(MPLocs.INGREDIENT, MPLocs.BURGER_CONSTRUCTOR)

    @allure.step('Проверяем счетчик ингредиента')
    def check_counter_ingredient(self, wait_time=TWTime.VISIBLE):
        ingred = MPLocs.COUNTER_INGREDIENT
        self.wait_for_visibility_element(ingred, wait_time)
        count = self.get_text(ingred)
        return int(count)
    
    @allure.step('Нажимаем на кнопку "Оформить заказ"')
    def click_button_create_order(self):
        self.click_on_element(MPLocs.BUTTON_CREATE_ORDER)

    @allure.step('Ожидаем появления окна id заказа')
    def wait_load_window_order_details(self, wait_time=TWTime.WINDOW):
        self.wait_for_visibility_element(MPLocs.ID_ORDER, wait_time)

    @allure.step('Ожидаем исчезновения затемнения')
    def wait_invisible_overlay(self, wait_time=TWTime.INVISIBLE):
        self.check_element_not_is_displayed(MPLocs.OVERLAY, wait_time)

    @allure.step('Получаем id заказа')
    def get_id_order(self, wait_time=TWTime.VISIBLE):
        id_order = MPLocs.ID_ORDER
        self.wait_for_visibility_element(id_order, wait_time)
        return self.get_text(id_order)
                                  
    
    @allure.step('Создаем заказ')
    def create_order(self):
        self.add_ingredient_to_order()
        self.click_button_create_order()
