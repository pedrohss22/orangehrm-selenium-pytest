
import sys
import os
import typing
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver

# Ajusta o caminho para importar o módulo `pages`
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'src')))
from pages.login_page import LoginPage

@pytest.fixture(scope="function")
def browser() -> typing.Generator[WebDriver, None, None]:
    driver = webdriver.Chrome()
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    yield driver
    driver.quit()

def test_successful_login(browser: WebDriver):
    login_page = LoginPage(browser)
    login_page.login("Admin", "admin123")
    assert login_page.is_login_successful()

def test_failed_login(browser: WebDriver):
    login_page = LoginPage(browser)
    login_page.login("Admin", "wrongpassword")
    assert not login_page.is_login_successful()