"""End-to-end checkout flow tests: login -> add to cart -> checkout info ->
overview -> confirmation. Mirrors playwright-suite/tests/ui/checkout.spec.ts.
"""
import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.checkout_page import CheckoutPage


def _login_as_standard_user(driver):
    LoginPage(driver).open_login_page().login("standard_user", "secret_sauce")
    return InventoryPage(driver)


def test_user_can_complete_a_full_purchase_end_to_end(driver):
    inventory_page = _login_as_standard_user(driver)
    checkout_page = CheckoutPage(driver)

    inventory_page.add_first_item_to_cart()
    checkout_page.go_to_cart()
    checkout_page.start_checkout()
    checkout_page.fill_checkout_info("Cristian", "Garcia", "760001")

    summary = checkout_page.get_order_summary()
    assert summary["total"] == pytest.approx(summary["subtotal"] + summary["tax"], abs=0.01)

    checkout_page.finish_order()
    assert checkout_page.is_order_complete()


def test_checkout_info_step_requires_all_fields_before_continuing(driver):
    inventory_page = _login_as_standard_user(driver)
    checkout_page = CheckoutPage(driver)

    inventory_page.add_first_item_to_cart()
    checkout_page.go_to_cart()
    checkout_page.start_checkout()
    checkout_page.continue_without_filling_info()

    assert "First Name is required" in checkout_page.get_error_message()
