from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from seletools.actions import drag_and_drop
from data import TestWaitTime as TWTime
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
    def wait_for_visibility_element(self, element, wait_time=TWTime.VISIBLE):
        WebDriverWait(self.driver, wait_time).until(EC.visibility_of_element_located(element))

    @allure.step('Ожидаем появление элемента страницы на экране')
    def check_element_is_displayed(self, element, wait_time=TWTime.VISIBLE):
        wait_element = WebDriverWait(self.driver, wait_time).until(EC.visibility_of_element_located(element))
        return wait_element.is_displayed()
    
    @allure.step('Ожидаем исчезновение элемента страницы с экрана')
    def check_element_not_is_displayed(self, element, wait_time=TWTime.INVISIBLE):
        return WebDriverWait(self.driver, wait_time).until(EC.invisibility_of_element_located(element))    

    @allure.step('Нажимаем на элемент страницы')
    def click_on_element(self, element):
        element = WebDriverWait(self.driver, TWTime.CLICKBLE).until(EC.element_to_be_clickable(element))
        self.driver.execute_script("arguments[0].click();", element)

    @allure.step('Получаем текст элемента')
    def get_text(self, element):
        return self.driver.find_element(*element).text

    @allure.step('Заполняем поле({placeholder})')
    def set_data(self, placeholder, data):
        self.driver.find_element(*placeholder).send_keys(data)

    @allure.step('Перетащить элемент на целевой элемент')
    def drag_and_drop_element(self, draggable_element, place_element):
        source = self.driver.find_element(*draggable_element)
        target = self.driver.find_element(*place_element)

        drag_and_drop(self.driver, source, target)
