from selenium.webdriver.common.by import By

class LoginPageLocators:
    USERNAME_FIELD = (By.NAME, "username")
    PASSWORD_FIELD = (By.NAME, "password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button.orangehrm-login-button")