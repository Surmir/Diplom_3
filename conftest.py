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
@pytest.fixture(scope='function', params=['firefox', 'chrome'])
def driver_main_page(request):
    driver = None

    if request.param == 'firefox':
        driver = webdriver.Firefox()
    elif request.param == 'chrome':
        driver = webdriver.Chrome()

    m_page = MainPage(driver)
    m_page.wait_load_main_page(7)

    yield driver

    driver.quit()

#запуск браузера с авторизацией
@pytest.fixture(scope='function', params=['firefox', 'chrome'])
def driver_with_auth(request):
    driver = None

    if request.param == 'firefox':
        driver = webdriver.Firefox()
    elif request.param == 'chrome':
        driver = webdriver.Chrome()

    l_page = LoginPage(driver)
    l_page.user_login(ULData.EMAIL, ULData.PASSWORD)

    yield driver

    driver.quit()
