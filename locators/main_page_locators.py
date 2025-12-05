from selenium.webdriver.common.by import By


class MainPageLocators():
    #заголовок главной страницы
    MAIN_PAGE_HEADER = (By.XPATH, ".//h1[text()='Соберите бургер']")
    #кнопка "Оформить заказ"(появляется после авторизации)
    BUTTON_CREATE_ORDER = (By.XPATH, ".//button[text()='Оформить заказ']")
    #идентификатор заказа
    ID_ORDER = (By.XPATH, ".//h2[@class='Modal_modal__title_shadow__3ikwq Modal_modal__title__2L34m text text_type_digits-large mb-8']")
    #ингредиент "Флюоресцентная булка R2-D3"
    INGREDIENT = (By.XPATH, ".//p[text()='Флюоресцентная булка R2-D3']")
    #окно "Детали ингредиента"
    WINDOW_INGR_DETAILS = (By.XPATH, ".//h2[text()='Детали ингредиента']")
    #кнопка "Х" закрывает детали ингредиента
    BUTTON_CLOSE_X = (By.XPATH, "(.//button[@class='Modal_modal__close_modified__3V5XS Modal_modal__close__TnseK'])[1]")
    #счетчик ингредиента
    COUNTER_INGREDIENT = (By.XPATH, "(.//p[@class='counter_counter__num__3nue1'])[1]")
    #конструктор бургера
    BURGER_CONSTRUCTOR = (By.XPATH, ".//ul[@class='BurgerConstructor_basket__list__l9dp_']")
