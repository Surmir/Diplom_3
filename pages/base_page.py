from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class BasePage():

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Переход на страницу {url}')
    def go_to_page(self, url):
        self.driver.get(url)

    @allure.step('Получаем URL страницы')
    def get_page_url(self):
        return self.driver.current_url
    
    @allure.step('Ожидаем видимости элемента страницы')
    def wait_for_visibility_element(self, element, wait_time=5):
        WebDriverWait(self.driver, wait_time).until(EC.visibility_of_element_located(element))

    @allure.step('Ожидаем открытия второго окна')
    def wait_new_window_is_opened(self, wait_time=5):
        WebDriverWait(self.driver, wait_time).until(EC.number_of_windows_to_be(2))

    @allure.step('Переходим в новое окно')
    def go_to_new_window(self):
        original_window = self.driver.current_window_handle
        for window_handle in self.driver.window_handles:
            if window_handle != original_window:
                self.driver.switch_to.window(window_handle)
                break

    @allure.step('Нажимаем на элемент страницы')
    def click_on_element(self, element):
        element = WebDriverWait(self.driver, 2).until(EC.element_to_be_clickable(element))
        element.click()

    @allure.step('Прокручиваем до элемента страницы')
    def skroll_to_element(self, element):
        element = self.driver.find_element(*element)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step('Получаем текст элемента')
    def get_text(self, element):
        return self.driver.find_element(*element).text

    @allure.step('Заполняем поле({placeholder})')
    def set_data(self, placeholder, data):
        self.driver.find_element(*placeholder).send_keys(data)
