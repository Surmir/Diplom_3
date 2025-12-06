from pages.base_page import BasePage
from locators.base_page_locators import BasePageLocators as BPLocs
from locators.feed_page_locators import FeedPageLocators as FPLocs
from urls import Url
import allure


class FeedPage(BasePage):

    @allure.step('Открываем страницу "Лента Заказов"')
    def open_feed_page(self):
        self.go_to_page(Url.FEED_PAGE)

    @allure.step('Ожидание загрузки страницы "Лента Заказов"')
    def wait_load_feed_page(self, time=5):
        self.wait_for_visibility_element(FPLocs.FEED_PAGE_HEADER, time)

    @allure.step('Нажимаем на кнопку "Конструктор" в шапке страницы')
    def click_button_builder(self):
        self.click_on_element(BPLocs.HEADER_BUTTON_BUILDER)

    @allure.step('Проверяем переход на главную страницу')
    def check_open_main_page(self):
        actual_url = self.get_page_url()
        expect_url = Url.MAIN_PAGE
        return actual_url == expect_url
    
    @allure.step('Проверяем счетчик «Выполнено за всё время»')
    def check_counter_completed_all_time(self):
        count = self.get_text(FPLocs.COUNTER_COMPLETED_ALL_TIME)
        return int(count)
    
    @allure.step('Проверяем счетчик «Выполнено за сегодня»')
    def check_counter_completed_today(self):
        count = self.get_text(FPLocs.COUNTER_COMPLETED_TODAY)
        return int(count)
    
    @allure.step('Проверяем раздел «В работе»')
    def check_section_in_work(self):
        return self.get_text(FPLocs.SECTION_IN_WORK)
