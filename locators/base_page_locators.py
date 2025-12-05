from selenium.webdriver.common.by import By


class BasePageLocators():
    #кнопка "Конструктор" в шапке страницы
    HEADER_BUTTON_BUILDER = (By.XPATH, ".//p[text()='Конструктор']")
    #кнопка "Лента Заказов" в шапке страницы
    HEADER_BUTTON_FEED = (By.XPATH, ".//p[text()='Лента Заказов']")
