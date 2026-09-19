"""Page Object for the SauceDemo login page (https://www.saucedemo.com)."""
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

URL = "https://www.saucedemo.com/"


class LoginPage(BasePage):
    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "[data-test='error']")

    def open_login_page(self):
        self.open(URL)
        return self

    def login(self, username: str, password: str):
        self.type(self.USERNAME_INPUT, username)
        self.type(self.PASSWORD_INPUT, password)
        self.click(self.LOGIN_BUTTON)
        return self

    def get_error_message(self) -> str:
        return self.text_of(self.ERROR_MESSAGE)
