from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
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

    @allure.step('Нажимаем на элемент страницы')
    def click_on_element(self, element):
        element = WebDriverWait(self.driver, 2).until(EC.element_to_be_clickable(element))
        element.click()

    @allure.step('Получаем текст элемента')
    def get_text(self, element):
        return self.driver.find_element(*element).text

    @allure.step('Заполняем поле({placeholder})')
    def set_data(self, placeholder, data):
        self.driver.find_element(*placeholder).send_keys(data)

    @allure.step('Перетащить элемент на целевой элемент')
    def drag_and_drop_element(self, draggable_element, place_element):
        actions = ActionChains(self.driver)
        source_element = self.driver.find_element(*draggable_element)
        target_element = self.driver.find_element(*place_element)
        actions.drag_and_drop(source_element, target_element).perform()
