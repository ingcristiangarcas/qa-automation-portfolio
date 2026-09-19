import { Page, Locator, expect } from '@playwright/test';

/**
 * Page Object covering the SauceDemo checkout flow: cart -> checkout info ->
 * overview -> confirmation. This is the critical business flow (an order
 * being placed end to end) that most demo portfolios skip in favor of only
 * testing login.
 */
export class CheckoutPage {
  readonly page: Page;
  readonly cartIcon: Locator;
  readonly checkoutButton: Locator;
  readonly firstNameInput: Locator;
  readonly lastNameInput: Locator;
  readonly postalCodeInput: Locator;
  readonly continueButton: Locator;
  readonly finishButton: Locator;
  readonly completeHeader: Locator;
  readonly summarySubtotal: Locator;
  readonly summaryTax: Locator;
  readonly summaryTotal: Locator;
  readonly errorMessage: Locator;

  constructor(page: Page) {
    this.page = page;
    this.cartIcon = page.locator('.shopping_cart_link');
    this.checkoutButton = page.locator('#checkout');
    this.firstNameInput = page.locator('#first-name');
    this.lastNameInput = page.locator('#last-name');
    this.postalCodeInput = page.locator('#postal-code');
    this.continueButton = page.locator('#continue');
    this.finishButton = page.locator('#finish');
    this.completeHeader = page.locator('.complete-header');
    this.summarySubtotal = page.locator('.summary_subtotal_label');
    this.summaryTax = page.locator('.summary_tax_label');
    this.summaryTotal = page.locator('.summary_total_label');
    this.errorMessage = page.locator('[data-test="error"]');
  }

  async goToCart() {
    await this.cartIcon.click();
  }

  async startCheckout() {
    await this.checkoutButton.click();
  }

  async fillCheckoutInfo(firstName: string, lastName: string, postalCode: string) {
    await this.firstNameInput.fill(firstName);
    await this.lastNameInput.fill(lastName);
    await this.postalCodeInput.fill(postalCode);
    await this.continueButton.click();
  }

  async finishOrder() {
    await this.finishButton.click();
  }

  async expectOrderComplete() {
    await expect(this.completeHeader).toHaveText('Thank you for your order!');
  }

  async getOrderSummary() {
    const subtotalText = await this.summarySubtotal.innerText();
    const taxText = await this.summaryTax.innerText();
    const totalText = await this.summaryTotal.innerText();

    return {
      subtotal: parseFloat(subtotalText.replace('Item total: $', '')),
      tax: parseFloat(taxText.replace('Tax: $', '')),
      total: parseFloat(totalText.replace('Total: $', '')),
    };
  }
}
