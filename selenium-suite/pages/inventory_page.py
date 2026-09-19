"""Page Object for the SauceDemo inventory (products) page."""
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class InventoryPage(BasePage):
    PAGE_TITLE = (By.CLASS_NAME, "title")
    INVENTORY_ITEMS = (By.CLASS_NAME, "inventory_item")
    ADD_TO_CART_BUTTONS = (By.CSS_SELECTOR, "button[id^='add-to-cart']")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    SORT_DROPDOWN = (By.CLASS_NAME, "product_sort_container")
    ITEM_PRICES = (By.CLASS_NAME, "inventory_item_price")

    def is_loaded(self) -> bool:
        return self.text_of(self.PAGE_TITLE) == "Products"

    def add_first_item_to_cart(self):
        buttons = self.find_all(self.ADD_TO_CART_BUTTONS)
        buttons[0].click()
        return self

    def get_cart_count(self) -> str:
        return self.text_of(self.CART_BADGE)

    def sort_by(self, value: str):
        from selenium.webdriver.support.ui import Select
        Select(self.find(self.SORT_DROPDOWN)).select_by_value(value)
        return self

    def get_item_prices(self) -> list:
        prices = self.find_all(self.ITEM_PRICES)
        return [float(p.text.replace("$", "")) for p in prices]
