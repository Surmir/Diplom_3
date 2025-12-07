import allure
from pages.main_page import MainPage
from pages.feed_page import FeedPage


class TestMainPage():

    @allure.title('Переход по клику на раздел «Лента заказов»')
    @allure.description('При нажатии кнопки «Лента заказов» в шапке страницы ' \
    'происходит переход в раздел «Лента заказов»')
    def test_feed_button_transition_to_feed_order(self, driver):
        m_page = MainPage(driver)
        f_page = FeedPage(driver)

        m_page.wait_open_and_load_main_page(15)
        m_page.click_button_feed()
        f_page.wait_load_feed_page(10)

        assert m_page.check_open_feed_page()

    @allure.title('Появление всплывающего окна "Детали ингредиента"')
    @allure.description('При клике на ингредиент, появляется всплывающее окно "Детали ингредиента"')
    def test_click_ingred_open_window_ingred_details(self, driver_main_page):
        m_page = driver_main_page

        m_page.click_ingredient()
        
        assert m_page.check_open_window_ingred_details(15)

    @allure.title('Закрытие всплывающего окна "Детали ингредиента"')
    @allure.description('При клике по крестику, закрывается всплывающее окно "Детали ингредиента"')
    def test_button_x_close_window_ingred_details(self, driver_main_page):
        m_page = driver_main_page

        m_page.click_ingredient()
        m_page.check_open_window_ingred_details(15)
        m_page.click_button_x()

        assert m_page.check_close_window_ingred_details(10)

    @allure.title('Увеличение счётчика ингредиента')
    @allure.description('При добавлении ингредиента в заказ счётчик этого ингредиента увеличивается')
    def test_add_ingred_to_order_counter_ingred_grow_up(self, driver_main_page):
        m_page = driver_main_page

        num_before = m_page.check_counter_ingredient(0)
        m_page.add_ingredient_to_order()
        num_after = m_page.check_counter_ingredient(5)

        assert num_before < num_after
