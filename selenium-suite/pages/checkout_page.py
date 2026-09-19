"""Page Object covering the SauceDemo checkout flow: cart -> checkout info ->
overview -> confirmation. Mirrors playwright-suite/pages/CheckoutPage.ts.
"""
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CheckoutPage(BasePage):
    CART_ICON = (By.CLASS_NAME, "shopping_cart_link")
    CHECKOUT_BUTTON = (By.ID, "checkout")
    FIRST_NAME_INPUT = (By.ID, "first-name")
    LAST_NAME_INPUT = (By.ID, "last-name")
    POSTAL_CODE_INPUT = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")
    FINISH_BUTTON = (By.ID, "finish")
    COMPLETE_HEADER = (By.CLASS_NAME, "complete-header")
    SUMMARY_SUBTOTAL = (By.CLASS_NAME, "summary_subtotal_label")
    SUMMARY_TAX = (By.CLASS_NAME, "summary_tax_label")
    SUMMARY_TOTAL = (By.CLASS_NAME, "summary_total_label")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "[data-test='error']")

    def go_to_cart(self):
        self.click_until_url_contains(self.CART_ICON, "cart.html")
        return self

    def start_checkout(self):
        self.click_until_url_contains(self.CHECKOUT_BUTTON, "checkout-step-one")
        return self

    def fill_checkout_info(self, first_name: str, last_name: str, postal_code: str):
        self.type(self.FIRST_NAME_INPUT, first_name)
        self.type(self.LAST_NAME_INPUT, last_name)
        self.type(self.POSTAL_CODE_INPUT, postal_code)
        self.click_until_url_contains(self.CONTINUE_BUTTON, "checkout-step-two")
        return self

    def continue_without_filling_info(self):
        self.click(self.CONTINUE_BUTTON)
        return self

    def finish_order(self):
        self.click_until_url_contains(self.FINISH_BUTTON, "checkout-complete")
        return self

    def is_order_complete(self) -> bool:
        return self.text_of(self.COMPLETE_HEADER) == "Thank you for your order!"

    def get_order_summary(self) -> dict:
        subtotal = float(self.text_of(self.SUMMARY_SUBTOTAL).replace("Item total: $", ""))
        tax = float(self.text_of(self.SUMMARY_TAX).replace("Tax: $", ""))
        total = float(self.text_of(self.SUMMARY_TOTAL).replace("Total: $", ""))
        return {"subtotal": subtotal, "tax": tax, "total": total}

    def get_error_message(self) -> str:
        return self.text_of(self.ERROR_MESSAGE)
