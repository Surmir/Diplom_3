from selenium.webdriver.common.by import By


class BasePageLocators():
    #кнопка "Конструктор" в шапке страницы
    HEADER_BUTTON_BUILDER = (By.XPATH, "(.//p[@class='AppHeader_header__linkText__3q_va ml-2'])[1]")
    #кнопка "Лента Заказов" в шапке страницы
    HEADER_BUTTON_FEED = (By.XPATH, "(.//p[@class='AppHeader_header__linkText__3q_va ml-2'])[2]")
