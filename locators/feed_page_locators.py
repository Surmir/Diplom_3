from selenium.webdriver.common.by import By


class FeedPageLocators():
    #заголовок страницы заказов
    FEED_PAGE_HEADER = (By.XPATH, ".//h1[text()='Лента заказов']")
    #счетчик «Выполнено за всё время»
    COUNTER_COMPLETED_ALL_TIME = (By.XPATH, "(.//p[@class='OrderFeed_number__2MbrQ text text_type_digits-large'])[1]")
    #счетчик «Выполнено за сегодня»
    COUNTER_COMPLETED_TODAY = (By.XPATH, "(.//p[@class='OrderFeed_number__2MbrQ text text_type_digits-large'])[2]")
    #раздел «В работе»
    SECTION_IN_WORK = (By.XPATH, ".//li[@class='text text_type_main-small']")
