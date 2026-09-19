"""Regression tests for the SauceDemo cart and product sorting flows."""
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


def _login_as_standard_user(driver):
    LoginPage(driver).open_login_page().login("standard_user", "secret_sauce")
    return InventoryPage(driver)


def test_add_item_to_cart_updates_badge_count(driver):
    inventory_page = _login_as_standard_user(driver)

    inventory_page.add_first_item_to_cart()

    assert inventory_page.get_cart_count() == "1"


def test_sort_products_by_price_low_to_high(driver):
    inventory_page = _login_as_standard_user(driver)

    inventory_page.sort_by("lohi")
    prices = inventory_page.get_item_prices()

    assert prices == sorted(prices), "Products should be sorted from lowest to highest price"


def test_sort_products_by_price_high_to_low(driver):
    inventory_page = _login_as_standard_user(driver)

    inventory_page.sort_by("hilo")
    prices = inventory_page.get_item_prices()

    assert prices == sorted(prices, reverse=True), "Products should be sorted from highest to lowest price"
