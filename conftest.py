import pytest
from selenium import webdriver


#запуск браузера
@pytest.fixture
def driver():
    driver = webdriver.Firefox()

    yield driver

    driver.quit()
