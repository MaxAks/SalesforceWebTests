import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture(scope="function") # Фиксутар вызова и закрытия браузера с инциацией для каждой функции в тесте
def browser():
    browser = webdriver.Chrome()
    yield browser
    browser.quit()