import pytest
from selenium import webdriver


#запуск браузера
@pytest.fixture(scope='function', params=['firefox', 'chrome'])
def browser(request):
    browser = None

    if request.param == 'firefox':
        browser = webdriver.Firefox()
    elif request.param == 'chrome':
        browser = webdriver.Chrome()

    yield browser

    browser.quit()
