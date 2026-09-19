"""Login flow tests for SauceDemo, covering valid, invalid and locked-out users."""
import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

STANDARD_USER = "standard_user"
LOCKED_USER = "locked_out_user"
PASSWORD = "secret_sauce"


def test_valid_login_redirects_to_inventory(driver):
    login_page = LoginPage(driver).open_login_page()
    login_page.login(STANDARD_USER, PASSWORD)

    inventory_page = InventoryPage(driver)
    assert inventory_page.is_loaded(), "Expected to land on the Products page after login"


def test_locked_out_user_sees_error_message(driver):
    login_page = LoginPage(driver).open_login_page()
    login_page.login(LOCKED_USER, PASSWORD)

    error = login_page.get_error_message()
    assert "locked out" in error.lower()


@pytest.mark.parametrize("username,password", [
    ("", ""),
    ("standard_user", "wrong_password"),
    ("unknown_user", "secret_sauce"),
])
def test_invalid_credentials_show_error(driver, username, password):
    login_page = LoginPage(driver).open_login_page()
    login_page.login(username, password)

    error = login_page.get_error_message()
    assert error, "Expected an error message for invalid credentials"
