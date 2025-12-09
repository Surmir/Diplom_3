import pytest
from selenium import webdriver
from pages.login_page import LoginPage
from pages.main_page import MainPage
from data import UserLoginData as ULData


#запуск браузера
@pytest.fixture(scope='function', params=['firefox', 'chrome'])
def driver(request):
    driver = None

    if request.param == 'firefox':
        driver = webdriver.Firefox()
    elif request.param == 'chrome':
        driver = webdriver.Chrome()

    yield driver

    driver.quit()

#запуск браузера с переходом на главную страницу
@pytest.fixture
def driver_main_page(driver):
    m_page = MainPage(driver)
    m_page.wait_open_and_load_main_page(20)

    return m_page

#запуск браузера с авторизацией
@pytest.fixture
def driver_with_auth(driver):
    l_page = LoginPage(driver)
    m_page = MainPage(driver)
    l_page.user_login(ULData.EMAIL, ULData.PASSWORD, 15)
    m_page.wait_load_main_page(10)

    return driver
