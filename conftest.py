import pytest
from selenium import webdriver
from pages.login_page import LoginPage
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
