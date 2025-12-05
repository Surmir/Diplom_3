from selenium.webdriver.common.by import By


class BasePageLocators():

    HEADER_BUTTON_BUILDER = (By.XPATH, ".//p[text()='Конструктор']")
    HEADER_BUTTON_FEED = (By.XPATH, ".//p[text()='Лента Заказов']")
