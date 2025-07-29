from selenium import webdriver
import pytest

@pytest.fixture(scope="module")
def browser():
    driver = webdriver.Chrome()  # You can change this to any other browser driver
    driver.implicitly_wait(10)
    yield driver
    driver.quit()