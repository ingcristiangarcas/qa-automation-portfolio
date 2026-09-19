import { Page, Locator, expect } from '@playwright/test';

export class InventoryPage {
  readonly page: Page;
  readonly pageTitle: Locator;
  readonly addToCartButtons: Locator;
  readonly cartBadge: Locator;
  readonly sortDropdown: Locator;
  readonly itemPrices: Locator;

  constructor(page: Page) {
    this.page = page;
    this.pageTitle = page.locator('.title');
    this.addToCartButtons = page.locator('button[id^="add-to-cart"]');
    this.cartBadge = page.locator('.shopping_cart_badge');
    this.sortDropdown = page.locator('.product_sort_container');
    this.itemPrices = page.locator('.inventory_item_price');
  }

  async expectLoaded() {
    await expect(this.pageTitle).toHaveText('Products');
  }

  async addFirstItemToCart() {
    await this.addToCartButtons.first().click();
  }

  async getCartCount(): Promise<string> {
    return this.cartBadge.innerText();
  }

  async sortBy(value: string) {
    await this.sortDropdown.selectOption(value);
  }

  async getItemPrices(): Promise<number[]> {
    const texts = await this.itemPrices.allInnerTexts();
    return texts.map((t) => parseFloat(t.replace('$', '')));
  }
}
