import allure
from pages.feed_page import FeedPage
from pages.main_page import MainPage


class TestFeedPage():

    @allure.title('Переход по клику на «Конструктор»')
    @allure.description('При нажатии кнопки «Конструктор» в шапке страницы ' \
    'происходит переход на главную страницу')
    def test_button_builder_transition_to_main_page(self, driver):
        f_page = FeedPage(driver)
        m_page = MainPage(driver)
        
        f_page.open_feed_page()
        f_page.wait_load_feed_page()
        f_page.click_button_builder()
        m_page.wait_load_main_page()

        assert  f_page.check_open_main_page()

    @allure.title('Увеличение счётчика «Выполнено за всё время»')
    @allure.description('При создании нового заказа счётчик «Выполнено за всё время» увеличивается')
    def test_create_new_order_counter_all_time_grow_up(self, driver_with_auth):
        f_page = FeedPage(driver_with_auth)
        m_page = MainPage(driver_with_auth)

        f_page.open_feed_page()
        f_page.wait_load_feed_page()
        num_before = f_page.check_counter_completed_all_time()

        m_page.open_main_page()
        m_page.wait_load_main_page()
        m_page.create_order()
        m_page.wait_load_window_order_details()

        f_page.open_feed_page()
        f_page.wait_load_feed_page()
        num_after = f_page.check_counter_completed_all_time()

        assert num_before < num_after

    @allure.title('Увеличение счётчика «Выполнено за сегодня»')
    @allure.description('При создании нового заказа счётчик «Выполнено за сегодня» увеличивается')
    def test_create_new_order_counter_today_grow_up(self, driver_with_auth):
        f_page = FeedPage(driver_with_auth)
        m_page = MainPage(driver_with_auth)

        f_page.open_feed_page()
        f_page.wait_load_feed_page()
        num_before = f_page.check_counter_completed_today()

        m_page.open_main_page()
        m_page.wait_load_main_page()
        m_page.create_order()
        m_page.wait_load_window_order_details()

        f_page.open_feed_page()
        f_page.wait_load_feed_page()
        num_after = f_page.check_counter_completed_today()

        assert num_before < num_after

    @allure.title('Номер заказа появляется в разделе «В работе»')
    @allure.description('После оформления заказа его номер появляется в разделе «В работе»')
    def test_create_new_order_section_in_work_show_id_order(self, driver_with_auth):
        f_page = FeedPage(driver_with_auth)
        m_page = MainPage(driver_with_auth)

        m_page.open_main_page()
        m_page.wait_load_main_page()
        m_page.create_order()
        m_page.wait_load_window_order_details()
        id_order = m_page.get_id_order()

        f_page.open_feed_page()
        f_page.wait_load_feed_page()
        section_in_work = f_page.check_section_in_work()

        assert id_order == section_in_work
